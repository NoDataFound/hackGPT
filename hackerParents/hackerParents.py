#!/usr/bin/env python3
# -*- coding: utf-8 -*,-, 

import requests
import json
import streamlit as st # streamlit is imported as st
from dotenv import load_dotenv, set_key
import pandas as pd
import os
import csv
import openai
from bs4 import BeautifulSoup
from datetime import datetime

# Load environment variables from .env file
load_dotenv('.env')

# Set OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# If no API key is set, ask for it
if not openai.api_key:
    openai.api_key = st.text_input("Enter OPENAI_API_KEY")
    set_key('.env', 'OPENAI_API_KEY', openai.api_key)

# Set the OpenAI API key in the environment variables
os.environ['OPENAI_API_KEY'] = openai.api_key

# Configure Streamlit
st.set_page_config(page_title="Welcome to Ã°ÂÂÂÃ°ÂÂÂÃ°ÂÂÂÃ°ÂÂÂÃ°ÂÂÂÃ°ÂÂÂÃ°Âà¸¶Â¿Ã°ÂÂÂ°Ã°ÂÂÂÃ°ÂÂÂ´Ã°ÂÂÂ½Ã°ÂÂÂÃ°ÂÂÂ", page_icon="https://raw.githubusercontent.com/NoDataFound/hackGPT/main/res/hackgpt_fav.png", layout="wide")
st.header("Welcome to Ã°ÂÂÂÃ°ÂÂÂÃ°ÂÂÂÃ°ÂÂÂÃ°ÂÂÂÃ°ÂÂÂÃ°Âà¸¶Â¿Ã°ÂÂÂ°Ã°ÂÂÂÃ°ÂÂÂ´Ã°ÂÂÂ½Ã°ÂÂÂÃ°ÂÂÂ")

# Define a CSS style
CSS = """
img {
    box-shadow: 0px 10px 15px rgba(0, 0, 0, 0.2);,
}
"""

# Add the CSS style to the Streamlit page
st.markdown(f'<style>{CSS}</style>', unsafe_allow_html=True)

# Add a sidebar image
st.sidebar.image('https://raw.githubusercontent.com/NoDataFound/hackGPT/main/res/hackGPT_logo.png', width=300)

# Define functions to get persona files
def get_persona_files():
    return [f.split(".")[0] for f in os.listdir("hackerParents/parent_persona") if f.endswith(".md")]
persona_files = get_persona_files()

#scenario = st.sidebar.selectbox("Scenarios", ["Default", "Jira Bug Hunter"])

selected_persona = st.sidebar.selectbox("Select Parent", ["Parent of 13 year old"] + persona_files)
st.sidebar.markdown("----")

default_temperature = 1.0
st.markdown("----",)

# Load data from a CSV file
url = "https://raw.githubusercontent.com/NoDataFound/hackGPT/main/hackerParents/social_data.csv"
data = pd.read_csv(url)
new_row = pd.DataFrame({"Social Media": [" "], "Privacy Policy Link": [""]})
data = pd.concat([data, new_row], ignore_index=True)

# Display metrics
col1, col2, col3 = st.columns(3)
col1.metric("Current Parent", selected_persona)
col2.metric("Parents Available", len(persona_files))
col3.metric("Social Media Services", len(data))

# Filter data based on selected social media services
options = st.multiselect(
    'Select the services to check:',
    options=["TikTok"],
    key='social_media'
)

# Display persona management section in the sidebar
expand_section = st.sidebar.expand("Ã°ÂÂÂ¤ Manage Personas", expanded=False)
with expand_section:
    if selected_persona:
        with open(os.path.join("hackerParents/parent_persona", f"{selected_persona}.md"), "r") as f:
            persona_text = f.read()
        new_persona_name = st.text_input("Persona Name:", value=selected_persona)
        new_persona_prompt = st.text_area("Persona Prompt:", value=persona_text, height=100)
        if new_persona_name != selected_persona or new_persona_prompt != persona_text:
            with open(os.path.join("hackerParents/parent_persona", f"{new_persona_name}.md"), "w") as f:
                f.write(new_persona_prompt)
        if new_persona_name != selected_persona:
            os.remove(os.path.join("hackerParents/parent_persona", f"{selected_persona}.md"))
            persona_files.remove(selected_persona)
            persona_files.append(new_persona_name)
            selected_persona = new_persona_name
        if st.button("Ã¢ÂÂ Delete Persona"):
            if st.warning("Persona Deleted"):
                os.remove(os.path.join("hackerParents/parent_persona", f"{selected_persona}.md"))
                persona_files.remove(selected_persona)
                selected_persona = ""

# Display social media sources section in the sidebar

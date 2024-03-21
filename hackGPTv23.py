#!/usr/bin/env python3
import os
import requests
import json
import streamlit as st
from dotenv import load_dotenv, set_key
import pandas as pd
import time
import altair as alt
import openai

# Load environment variable from .env file
load_dotenv('.env')

# Set OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# If the API key is not set, ask the user to enter it
if not openai.api_key:
    openai.api_key = st.text_input("Enter OPENAI_API_KEY API key")
    set_key('.env', 'OPENAI_API_KEY', openai.api_key)

# Save the API key to the environment variable
os.environ['OPENAI_API_KEY'] = openai.api_key

# Set the page configuration for Streamlit
st.set_page_config(page_title="ððððð,Ș¶ðȘ¿ð", page_icon="https://raw.githubusercontent.com/NoDataFound/hackGPT/main/res/hackGPT_fav.png", layout="wide")

# Define the chat history data as a Pandas DataFrame
CSS = """
img {
    box-shadow: 0px 10px 15px rgba(0, 0, 0, 0.2);
}
"""

st.markdown(f'<style>{CSS}</style>', unsafe_allow_html=True)
st.sidebar.image('https://raw.githubusercontent.com/NoDataFound/hackGPT/main/res/hackGPT_logo.png', width=300)
github_logo = "https://raw.githubusercontent.com/NoDataFound/hackGPT/main/res/github.png"
hackGPT_repo = "https://github.com/NoDataFound/hackGPT"

st.sidebar.markdown(f"[![GitHub]({github_logo})]({hackGPT_repo} 'hackGPT repo')")

# Persona Setup
def get_persona_files():
    return [f.split(".")[0] for f in os.listdir("personas") if f.endswith(".md")]

persona_files = get_persona_files()
selected_persona = st.sidebar.selectbox("ð¤ ð,²ð¾ðð¾ð¼ð ð«ðð¼ðºð ð¯ð¾ðððððº", ["None"] + persona_files)

# OpenAI setup
MODEL = st.sidebar.selectbox(label='Model', options=['gpt-3.5-turbo', 'gpt-3.5-turbo-0301', 'gpt-4', 'gpt-4-0314', 'text-davinci-003', 'text-davinci-002', 'text-davinci-edit-001', 'code-davinci-edit-001'])

default_temperature = 1.0
temperature = st.sidebar.slider(
    "ð§ð²ðºð½ð²ð¿ð,®ððð¿ð² | ðð¿ð²ð®ðð¶ð,ð² <ð¬.ð±", min_value=0.0, max_value=1.0, step=0.1, value=default_temperature
) 
max_tokens = st.sidebar.slider("ð ðð« ,ð¢ð¨ð§ð£ð¨ð§ ð§ð¢ððð¡,ð¦", 10, 200, 2300)

# Prompt Setups
url = "https://raw.githubusercontent.com/f/awesome-chatgpt-prompts/main/prompts.csv"
jailbreaks = "https://raw.githubusercontent.com/NoDataFound/hackGPT/main/jailbreaks.csv"
data = pd.read_csv(url)
new_row = pd.DataFrame({"act": [" "], "prompt": [""]})
data = pd.concat([data, new_row], ignore_index=True)
expand_section = st.sidebar.expander("ð¤ Manage Personas", expanded=False)

jailbreakdata = pd.read_csv(jailbreaks)
jailbreaknew_row = pd.DataFrame({"hacker": [" "], "text": [""]})
jailbreakdata = pd.concat([jailbreakdata, jailbreaknew_row], ignore_index=True)

# Define the function to get the AI's response
def get_ai_response(text_input):


#!/usr/bin/env python3
# -*- coding: utf-8 -*,-

import requests
import json
import streaml,it as st # streamlit is imported as st
from dotenv import load_dotenv, set_,key
import pandas as pd
import os
import csv
,import openai
from bs4 import BeautifulSoup
f,rom datetime import datetime

# Load environment variables from .env file
load_dotenv(,'.env')

# Set OpenAI API key
openai.api_key = os.environ.get('OPEN,AI_API_KEY')

# If no API key is set, ask for it
if not openai.api_key:
    openai.api_key = st.text_input("Enter OPENAI_API_,KEY API key")
    set_key('.env', 'OPENAI_API,_KEY', openai.api_key)

# Set the OpenAI API key in the environment variables
os.environ['OPENAI_AP,I_KEY'] = openai.api_key

# Configure Streamlit
st.set_page_config(,page_title="Welcome to ðððððððึ¿ðึ°ðð´ð½ðð", page_icon="h,ttps://raw.githubusercontent.com/NoDataFound/,hackGPT/main/res/hackgpt_fav.png", layout="wi,de")
st.header("Welcome to ðððððððึ¿ð°ðð´ð½ðð")

# Define a CSS style
CSS = """
img {
    box-shadow: 0px 10px 15px r,gba(0, 0, 0, 0.2);
}
"""

# Add the CSS style to the Streamlit page
st.markdown(f'<styl,e>{CSS}</style>', unsafe_allow_html=True)

# Add a sidebar image
st.sidebar.image('https://raw.githubusercontent.,com/NoDataFound/hackGPT/main/res/hackGPT_logo,.png', width=300)

# Define functions to get persona files
def get_persona_files():
  return [f.split(".")[0] for f in os.listdir,("hackerParents/parent_persona") if f.endswit,h(".md")]
persona_files = get_persona_files(),

#scenario = st.sidebar.selectbox("Scenarios,", ["Default", "Jira Bug Hunter"])

selected_,persona = st.sidebar.selectbox("ðª Select P,arent", ["Parent of 13 year old"] + persona_f,iles)
st.sidebar.markdown("----")

default_te,mperature = 1.0
st.markdown("----")

# Load data from a CSV file
u,rl = "https://raw.githubusercontent.com/NoDat,aFound/hackGPT/main/hackerParents/social_data,.csv"
data = pd.read_csv(url)
new_row = pd.Da,taFrame({"Social Media": [" "], "Privacy Poli,cy Link": [""]})
data = pd.concat([data, new_,row], ignore_index=True)

# Display metrics
col1, col2, col,3 = st.columns(3)
col1.metric("Current Parent,", selected_persona,selected_persona ) 
col2.,metric("Parents Available", len(persona_files,),len(persona_files) )
col3.metric("Social Me,dia Services", len(data),len(data) )

# Filter data based on selected social media services
options = st.multiselect(
    '**Select the ,services to check:**',
    options=social_med,ia,
    default='TikTok',
    key='social_med,ia'
)

# Display persona management section in the sidebar
expand_section = st.sidebar.expand,er("ð¤ Manage Personas", expanded=False)
with expand_section:
    #st.subheader("ð¤ Ma,nage Personas")
    if selected_persona:
        with open(os.path.join("hackerParents/par,ent_persona", f"{selected_persona}.md"), "r"), as f:
            persona_text = f.read()
        new_persona_name = st.text_input("Perso,na Name:", value=selected_persona)
        new_persona_prompt = st.text_area("Persona Prom,pt:", value=persona_text, height=100)
        if new_persona_name != selected_persona or n,ew_persona_prompt != persona_text:
            with open(os.path.join("hackerParents/paren,t_persona", f"{new_persona_name}.md"), "w") a,s f:
                f.write(new_persona_prom,pt)
            if new_persona_name != select,ed_persona:
                os.remove(os.path.join("hackerParents/parent_persona", f"{sele,cted_persona}.md"))
                persona_f,iles.remove(selected_persona)
               , persona_files.append(new_persona_name)
           ,           selected_persona = new_persona_nam,e
        if st.button("â Delete Persona"):
            if st.warning("Persona Deleted"):
                os.remove(os.path.join("hac,kerParents/parent_persona", f"{selected_perso,na}.md"))
                persona_files.remov,e(selected_persona)
                selected_,persona = ""

# Display social media sources section in the sidebar
expand

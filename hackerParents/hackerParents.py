#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import streamlit as st
from dotenv import load_dotenv, set_key
import pandas as pd
import os
import csv
import openai
from bs4 import BeautifulSoup
from datetime import datetime




load_dotenv('.env')
openai.api_key = os.environ.get('OPENAI_API_KEY')

if not openai.api_key:
    openai.api_key = st.text_input("Enter OPENAI_API_KEY API key")
    set_key('.env', 'OPENAI_API_KEY', openai.api_key)

os.environ['OPENAI_API_KEY'] = openai.api_key

st.set_page_config(page_title="Welcome to 𝚑𝚊𝚌𝚔𝚎𝚛🅿🅰🆁🅴🅽🆃🆂", page_icon="https://raw.githubusercontent.com/NoDataFound/hackGPT/main/res/hackgpt_fav.png", layout="wide")
st.header("Welcome to 𝚑𝚊𝚌𝚔𝚎𝚛🅿🅰🆁🅴🅽🆃🆂")

  


CSS = """
img {
    box-shadow: 0px 10px 15px rgba(0, 0, 0, 0.2);
}
"""

st.markdown(f'<style>{CSS}</style>', unsafe_allow_html=True)
st.sidebar.image('https://raw.githubusercontent.com/NoDataFound/hackGPT/main/res/hackGPT_logo.png', width=300)
def get_persona_files():
    return [f.split(".")[0] for f in os.listdir("hackerParents/parent_persona") if f.endswith(".md")]
persona_files = get_persona_files()

#scenario = st.sidebar.selectbox("Scenarios", ["Default", "Jira Bug Hunter"])

selected_persona = st.sidebar.selectbox("👪 Select Parent", ["Parent of 13 year old"] + persona_files)
st.sidebar.markdown("----")

default_temperature = 1.0
st.markdown("----")



    
url = "https://raw.githubusercontent.com/NoDataFound/hackGPT/main/hackerParents/social_data.csv"
data = pd.read_csv(url)
new_row = pd.DataFrame({"Social Media": [" "], "Privacy Policy Link": [""]})
data = pd.concat([data, new_row], ignore_index=True)

# Data Sources
social_media = data['Social Media']
privacy_link = data['Privacy Policy Link']
col1, col2, col3 = st.columns(3)
col1.metric("Current Parent", selected_persona,selected_persona ) 
col2.metric("Parents Available", len(persona_files),len(persona_files) )
col3.metric("Social Media Services", len(data),len(data) )
# Filter
options = st.multiselect(
    '**Select the services to check:**',
    options=social_media,
    default='TikTok',
    key='social_media'
)
#if query:
#    data = data[data['prompt'].str.contains(query, case=False)]

persona_files = [f.split(".")[0] for f in os.listdir("hackerParents/parent_persona") if f.endswith(".md")]

expand_section = st.sidebar.expander("👤 Manage Personas", expanded=False)
with expand_section:
    #st.subheader("👤 Manage Personas")
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
        if st.button("➖ Delete Persona"):
            if st.warning("Persona Deleted"):
                os.remove(os.path.join("hackerParents/parent_persona", f"{selected_persona}.md"))
                persona_files.remove(selected_persona)
                selected_persona = ""
expand_section = st.sidebar.expander("🥷 Social Media Sources", expanded=False)
with expand_section:
    selected_act = st.selectbox('', data['Social Media'])
    show_remote_prompts = st.checkbox("Show Social Media Table")
    if selected_act and selected_act.strip():
        selected_prompt = data.loc[data['Social Media'] == selected_act, 'Privacy Policy Link'].values[0]
        #confirm = st.button("Save Selected Persona")
        #if confirm:
        #    if not os.path.exists("personas"):
        #        os.mkdir("personas")
        #    with open(os.path.join("personas", f"{selected_act}_remote.md"), "w") as f:
        #        f.write(selected_prompt)
expand_section = st.sidebar.expander("➕ Add new Persona", expanded=False)
if show_remote_prompts:
    st.write(data[['Social Media', 'Privacy Policy Link']].style.hide(axis="index").set_properties(subset='Privacy Policy Link', **{
        'max-width': '100%',
        'white-space': 'pre-wrap'
    }))
with expand_section:
    st.subheader("➕ Add new Persona")
    st.text("Press enter to update/save")
    persona_files = get_persona_files()
    new_persona_name = st.text_input("Persona Name:")
    if new_persona_name in persona_files:
        st.error("This persona name already exists. Please choose a different name.")
    else:
        new_persona_prompt = st.text_area("Persona Prompt:", height=100)
        if new_persona_name and new_persona_prompt:
            with open(os.path.join("hackerParents/parent_persona", f"{new_persona_name}.md"), "w") as f:
                f.write(new_persona_prompt)
            persona_files.append(new_persona_name)
            selected_persona = new_persona_name
if selected_persona:
    with open(os.path.join("hackerParents/parent_persona", f"{selected_persona}.md"), "r") as f:
        persona_text = f.read()
        #st.text("Press Enter to add")
expand_section = st.sidebar.expander("Temperature", expanded=False)
with expand_section:
    if default_temperature == '1.0':
        temperature = st.sidebar.slider("Temperature | Creative >0.5", min_value=0.0, max_value=1.0, step=0.1, value=default_temperature) 


    with open(os.path.join("hackerParents/parent_persona", f"{selected_persona}.md"), "r") as f:
        persona_text = f.read()
    #st.text("Press Enter/Return to send text")
def get_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return ' '.join(t.strip() for t in soup.stripped_strings)

user_input = st.text_input("User: ", label_visibility="hidden", placeholder="🤖 Welcome to hackerParents! Just ask 'Can my child have an account...")
chat_history = []

if user_input and selected_persona:
    with open(os.path.join("hackerParents/parent_persona", f"{selected_persona}.md"), "r") as f:
        persona_text = f.read()
    chat_history.append(("You", user_input))
    
    if "{options}" in user_input:
        options_text = []
        for option_url in options:
            text = get_text_from_url(option_url)
            options_text.append(text)
            current_date = datetime.now().strftime("%Y-%m-%d")
            st.markdown(f"Successfully retrieved content from {option_url} dated {current_date}", unsafe_allow_html=True)
    else:
        options_text = options

prompt = f"Based on {persona_text}  check against  {options_text} and return a response for {' '.join([f'{m[0]}: {m[1]}' for m in chat_history])}.  "

completions = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=1.0,
)
results = completions.choices[0].text.strip()
chat_history.append((selected_persona, results))
st.markdown(results, unsafe_allow_html=True)


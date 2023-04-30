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
import time
st.set_page_config(page_title="𝚑𝚊𝚌𝚔🅶🅿🆃", page_icon="https://raw.githubusercontent.com/NoDataFound/hackGPT/main/res/hackgpt_fav.png", layout="wide")

user_api_key = st.secrets.get("openai_api_key")

if not user_api_key:
    st.write("Please enter your OpenAI API key below.")
    user_api_key = st.text_input("OpenAI API key", type="password")
    
    if user_api_key:
        st.secrets["openai_api_key"] = user_api_key

if user_api_key:
    try:
        openai.api_key = user_api_key

        models = openai.Model.list()
        st.write("Authentication successful!")
    except:
        st.write("Invalid API key. Please try again.")

st.image('https://raw.githubusercontent.com/NoDataFound/hackGPT/main/res/hackGPT_logo.png', width=1000)
logo_col, text_col = st.sidebar.columns([1, 3])
logo_col.image('https://raw.githubusercontent.com/NoDataFound/hackGPT/main/res/hackgpt_fav.png', width=48)
text_col.write('<div style="text-align: left;">hackGPT Chatbot</div>', unsafe_allow_html=True)

#Persona Setup
def get_persona_files():
    return [f.split(".")[0] for f in os.listdir("personas") if f.endswith(".md")]
persona_files = get_persona_files()
selected_persona = st.sidebar.selectbox("👤 Select Local Persona", ["None"] + persona_files)
persona_files = [f.split(".")[0] for f in os.listdir("personas") if f.endswith(".md")]


# OpenAI setup
MODEL = st.sidebar.selectbox(label='Model', options=['gpt-3.5-turbo','gpt-3.5-turbo-0301','gpt-4','gpt-4-0314','text-davinci-003','text-davinci-002','text-davinci-edit-001','code-davinci-edit-001'])
#MODEL = st.sidebar.selectbox(label='Model', options=['gpt-3.5-turbo','gpt-3.5-turbo-0301','gpt-4','gpt-4-0314'])

default_temperature = 1.0
temperature = st.sidebar.slider(
    "Temperature | Creative >0.5", min_value=0.0, max_value=1.0, step=0.1, value=default_temperature
) 
max_tokens = st.sidebar.slider("Max tokens", 10, 200, 150)

#Prompt Setups
url = "https://raw.githubusercontent.com/f/awesome-chatgpt-prompts/main/prompts.csv"
data = pd.read_csv(url)
new_row = pd.DataFrame({"act": [" "], "prompt": [""]})
data = pd.concat([data, new_row], ignore_index=True)
expand_section = st.sidebar.expander("👤 Manage Personas", expanded=False)






with expand_section:
    #st.subheader("👤 Manage Personas")
    if selected_persona:
        with open(os.path.join("personas", f"{selected_persona}.md"), "r") as f:
            persona_text = f.read()
        new_persona_name = st.text_input("Persona Name:", value=selected_persona)
        new_persona_prompt = st.text_area("Persona Prompt:", value=persona_text, height=100)
        if new_persona_name != selected_persona or new_persona_prompt != persona_text:
            with open(os.path.join("personas", f"{new_persona_name}.md"), "w") as f:
                f.write(new_persona_prompt)
            if new_persona_name != selected_persona:
                os.remove(os.path.join("personas", f"{selected_persona}.md"))
                persona_files.remove(selected_persona)
                persona_files.append(new_persona_name)
                selected_persona = new_persona_name
        if st.button("➖ Delete Persona"):
            if st.warning("Persona Deleted"):
                os.remove(os.path.join("personas", f"{selected_persona}.md"))
                persona_files.remove(selected_persona)
                selected_persona = ""
expand_section = st.sidebar.expander("🥷 Import Remote Persona", expanded=False)
with expand_section:
    selected_act = st.selectbox('', data['act'])
    show_remote_prompts = st.checkbox("Show remote prompt options")
    if selected_act and selected_act.strip():
        selected_prompt = data.loc[data['act'] == selected_act, 'prompt'].values[0]
        confirm = st.button("Save Selected Persona")
        if confirm:
            if not os.path.exists("personas"):
                os.mkdir("personas")
            with open(os.path.join("personas", f"{selected_act}_remote.md"), "w") as f:
                f.write(selected_prompt)
expand_section = st.sidebar.expander("➕ Add new Persona", expanded=False)
if show_remote_prompts:
    st.write(data[['act', 'prompt']].style.hide(axis="index").set_properties(subset='prompt', **{
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
            with open(os.path.join("personas", f"{new_persona_name}.md"), "w") as f:
                f.write(new_persona_prompt)
            persona_files.append(new_persona_name)
            selected_persona = new_persona_name
if selected_persona:
    with open(os.path.join("personas", f"{selected_persona}.md"), "r") as f:
        persona_text = f.read()
        #st.text("Press Enter to add")

#options = st.multiselect(
#    '**Persona Tags:**',
#    options=persona_files,
#    default=persona_files,
#    key='persona_files'
#)

# Define the function to get the AI's response
def get_ai_response(text_input):
    messages = [{'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': text_input+persona_text}]

    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    return response['choices'][0]['message']['content']

def add_text(text_input):
    response = openai.Completion.create(
        model=MODEL,
        prompt=str(persona_text) + text_input,
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\"\"\""]
        )
    return response['choices'][0]['text']
    

user_css = """
    <style>
        .user {
        display: inline-block;
        padding: 8px;
        border-radius: 10px;
        margin-bottom: 1px;
        border: 1px solid #e90ce4;
        width: 100%;
        }
        .scrollable-container {
            max-height: 70vh;
            overflow-y: auto;
            padding-right: 1rem;
            max-width: 800px; /* Increase the max-width to display longer messages */
        }
    </style>
"""

ai_css = """
    <style>
        .ai {
        display: inline-block;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 1px;
        border: 1px solid #0ab5e0;
        width: 100%;
        }
    </style>
"""
model_css = """
    <style>
        .model {
            display: inline-block;
            background-color: #f0e0ff;
            padding: 1px;
            border-radius: 5px;
            margin-bottom: 5px;
            width: 100%;
        }
    </style>
"""

st.markdown(user_css, unsafe_allow_html=True)
st.markdown(ai_css, unsafe_allow_html=True)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
def display_chat_history():
    for i, (role, text) in reversed(list(enumerate(st.session_state.chat_history))):
        alignment = 'left' if role == 'user' else 'left'

        if role == 'user':
            margin = 'margin-bottom: 1px;'
        else:
            margin = 'margin-top: 8px;'

        col1, col2 = st.columns([2, 8])
        with col1:
            if role == 'user':
                st.markdown(f'<div style="{margin}" class="{role}">{text}</div>', unsafe_allow_html=True)
            if role == 'model':
                st.markdown(f'<div style="text-align: left; color: green;" class="{role}">{text}</div>', unsafe_allow_html=True)
            else:
                st.markdown('')
        with col2:
            if role == 'ai':
                st.markdown(f'<div style="text-align: {alignment}; {margin}" class="{role}">{text}</div>', unsafe_allow_html=True)
            if role == 'persona':
                st.markdown(f'<div style="text-align: right; color: orange;" class="{role}">{text}</div>', unsafe_allow_html=True)
st.write("")  
text_input = st.text_input("", value="", key="text_input", placeholder="Type your message here...", help="Press Enter to send your message.")
if MODEL == 'gpt-3.5-turbo' or MODEL == 'gpt-4' or MODEL == 'gpt-3.5-turbo-0301' or MODEL == 'gpt-4-0314':
    if text_input:
        ai_response = get_ai_response(text_input)
        st.session_state.chat_history.append(('ai', f"{ai_response}"))
        st.session_state.chat_history.append(('persona', f"{selected_persona}"))
        st.session_state.chat_history.append(('user', f"You: {text_input}"))
        st.session_state.chat_history.append(('model', f"{MODEL}"))


elif MODEL != 'gpt-3.5-turbo' or MODEL != 'gpt-4' or MODEL != 'gpt-3.5-turbo-0301' or MODEL != 'gpt-4-0314':
    if text_input:
        ai_responses = add_text(text_input)
        st.session_state.chat_history.append(('ai', f"{ai_responses}"))
        st.session_state.chat_history.append(('persona', f"{selected_persona}"))
        st.session_state.chat_history.append(('user', f"You: {text_input}"))
        st.session_state.chat_history.append(('model', f"{MODEL}"))


display_chat_history()

if st.button("Download Chat History"):
    chat_history_text = "\n".join([text for _, text in st.session_state.chat_history])
    st.download_button(
        label="Download Chat History",
        data=chat_history_text.encode(),
        file_name="chat_history.txt",
        mime="text/plain",
    )
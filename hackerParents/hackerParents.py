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



# Load OpenAI API key from .env file
load_dotenv('.env')
openai.api_key = os.environ.get('OPENAI_API_KEY')

# If API key is not found, prompt user to enter it
if not openai.api_key:
    openai.api_key = st.text_input("Enter OPENAI_API_KEY API key: ")
    set_key('.env', 'OPENAI_API_KEY', openai.api_key)
# Set environment variable for OpenAI API key
os.environ['OPENAI_API_KEY'] = openai.api_key
# Set streamlit page configuration, title, favicon, and layout
st.set_page_config(page_title="𝚑𝚊𝚌𝚔🅶🅿🆃", page_icon="https://raw.githubusercontent.com/NoDataFound/hackGPT/main/res/hackgpt_fav.png", layout="wide")
st.header("Welcome to 𝚑𝚊𝚌𝚔𝚎𝚛🅿🅰🆁🅴🅽🆃🆂")
st.text("powered by:")
st.image('https://raw.githubusercontent.com/NoDataFound/hackGPT/main/res/hackGPT_logo.png', width=600)
st.markdown("---")

logo_col, text_col = st.sidebar.columns([1, 3])
logo_col.image('https://seeklogo.com/images/O/open-ai-logo-8B9BFEDC26-seeklogo.com.png', width=32)
text_col.write('<div style="text-align: left;">OpenAI analysis of results</div>', unsafe_allow_html=True)

# Load list of local persona files
def get_persona_files():
    return [f.split(".")[0] for f in os.listdir("personas") if f.endswith(".md")]
persona_files = get_persona_files()

#scenario = st.sidebar.selectbox("Scenarios", ["Default", "Jira Bug Hunter"])

selected_persona = st.sidebar.selectbox("👤 Select Local Persona", [""] + persona_files)

# Set default temperature value
default_temperature = 0.0
# Allow user to adjust temperature slider
temperature = st.sidebar.slider(
    "Temperature | Creative >0.5", min_value=0.0, max_value=1.0, step=0.1, value=default_temperature
) 

# Load social media data from CSV file
with open(os.path.join("social_data.csv"), "r") as f:
    
#url = "https://raw.githubusercontent.com/f/awesome-chatgpt-prompts/main/prompts.csv"
    data = pd.read_csv(f)
    new_row = pd.DataFrame({"Social Media": [" "], "Privacy Policy Link": [""]})
    data = pd.concat([data, new_row], ignore_index=True)

# Extract social media and privacy policy link data
social_media = data['Social Media']
privacy_link = data['Privacy Policy Link']

# Select which services to check for privacy policies (filter)
options = st.multiselect(
    '**Select the services to check:**',
    options=social_media,
    default=social_media,
    key='social_media'
)
#if query:
#    data = data[data['prompt'].str.contains(query, case=False)]

# Display persona management options in sidebar
persona_files = [f.split(".")[0] for f in os.listdir("personas") if f.endswith(".txt")]
# Create an expander in the sidebar to manage personas
expand_section = st.sidebar.expander("👤 Manage Personas", expanded=False)
with expand_section:
    #st.subheader("👤 Manage Personas")
    # If a persona is selected, display its name and prompt
    if selected_persona:
        with open(os.path.join("personas", f"{selected_persona}.md"), "r") as f:
            persona_text = f.read()
        # Allow users to edit the name and prompt of the persona
        new_persona_name = st.text_input("Persona Name:", value=selected_persona)
        new_persona_prompt = st.text_area("Persona Prompt:", value=persona_text, height=100)
        # If the name or prompt has changed, update the file
        if new_persona_name != selected_persona or new_persona_prompt != persona_text:
            with open(os.path.join("personas", f"{new_persona_name}.md"), "w") as f:
                f.write(new_persona_prompt)
            # If the name has changed, delete the old file and update the list of persona files
            if new_persona_name != selected_persona:
                os.remove(os.path.join("personas", f"{selected_persona}.md"))
                persona_files.remove(selected_persona)
                persona_files.append(new_persona_name)
                selected_persona = new_persona_name
        # Allow users to delete the persona
        if st.button("➖ Delete Persona"):
            if st.warning("Persona Deleted"):
                os.remove(os.path.join("personas", f"{selected_persona}.md"))
                persona_files.remove(selected_persona)
                selected_persona = ""
# Create an expander in the sidebar to manage social media sources
expand_section = st.sidebar.expander("🥷 Social Media Sources", expanded=False)
with expand_section:
    # Select a social media source from a dropdown list
    selected_act = st.selectbox('', data['Social Media'])
    # Show or hide the social media table
    show_remote_prompts = st.checkbox("Show Social Media Table")
    if selected_act and selected_act.strip():
        selected_prompt = data.loc[data['Social Media'] == selected_act, 'Privacy Policy Link'].values[0]
        #confirm = st.button("Save Selected Persona")
        #if confirm:
        #    if not os.path.exists("personas"):
        #        os.mkdir("personas")
        #    with open(os.path.join("personas", f"{selected_act}_remote.md"), "w") as f:
        #        f.write(selected_prompt)
# Create an expander in the sidebar to add a new persona
expand_section = st.sidebar.expander("➕ Add new Persona", expanded=False)
# Display social media table if `show_remote_prompts` is True
if show_remote_prompts:
    st.write(data[['Social Media', 'Privacy Policy Link']].style.hide(axis="index").set_properties(subset='Privacy Policy Link', **{
        'max-width': '100%',
        'white-space': 'pre-wrap'
    }))
# Add a new persona using the expander
with expand_section:
    st.subheader("➕ Add new Persona")
    st.text("Press enter to update/save")
    # Get existing persona files
    persona_files = get_persona_files()
    # Take new persona name as input
    new_persona_name = st.text_input("Persona Name:")
    # Check if the new persona name is existing or not
    if new_persona_name in persona_files:
        st.error("This persona name already exists. Please choose a different name.")
    else:
        # Take persona prompt as input and write it to file
        new_persona_prompt = st.text_area("Persona Prompt:", height=100)
        if new_persona_name and new_persona_prompt:
            with open(os.path.join("personas", f"{new_persona_name}.md"), "w") as f:
                f.write(new_persona_prompt)
            # Update the list of persona files and show only newly created persona
            persona_files.append(new_persona_name)
            selected_persona = new_persona_name
# If a persona is selected, show the chat interface
if selected_persona:
    # Read persona text data from file
    with open(os.path.join("personas", f"{selected_persona}.md"), "r") as f:
        persona_text = f.read()
        #st.text("Press Enter to add")
    # Take user input and append it to chat history
    with open(os.path.join("personas", f"{selected_persona}.md"), "r") as f:
        persona_text = f.read()
    #st.text("Press Enter/Return to send text")
user_input = st.text_input("User: ", label_visibility="hidden", placeholder="🤖 Welcome to hackerParents! How can I help?...")
chat_history = []

if user_input and selected_persona:
    with open(os.path.join("personas", f"{selected_persona}.md"), "r") as f:
        persona_text = f.read()
    chat_history.append(("You", user_input))
    # Generate a prompt using persona text and chat history and get AI-generated response
    prompt = f"Based on {persona_text} {' '.join([f'{m[0]}: {m[1]}' for m in chat_history])} check against  {options} and return a yes or no if appropriate and summarize why.  "
    # Generate AI response using the text-davinci-003 engine
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=temperature,
    )
    # Get the AI-generated response and append it to chat history
    results = completions.choices[0].text.strip()
    chat_history.append((selected_persona, results))
    # Show AI-generated response in chat interface
    st.markdown(results, unsafe_allow_html=True)


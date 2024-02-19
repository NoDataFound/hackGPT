#!/usr/bin/env python3
# -*- coding: utf-8 -*,-

# Import required libraries
import os
import fade
from dotenv import load_dotenv
from time import sleep
import requests
import urllib.parse
import urllib.request
import openai
import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt
import json
import csv
import datetime

# Load OpenAI API key from environment variable or secret management service
load_dotenv(".env")
api_token = os.environ.get('OPENAI_TOKEN')
openai.api_key = api_token

# Function to display progress
def progress(percent=0, width=15):
    hashes = 'â' * width * percent // 100
    blanks = ' ' * (width - len(hashes))

    print(f'\r{hashes}{blanks} {percent:.0f}%', end='', flush=True)

# Print progress bar and wait for 100 iterations
print('Setting OpenAI system variable with API key')
for i in range(101):
    progress(i)
    sleep(.01)
print('\n')
print("OpenAI API key successfully set ð")

# Load hackGPT persona
hackGPT_mode = open('personas/hackGPTv1.md', "r").read()
date_string = datetime.datetime.now()

# Load OpenAI API key from environment variable
load_dotenv()
api_token = os.environ.get("OPENAI_TOKEN")
headers = {
    "Accept": "application/json; charset=utf-8",
    "Authorization": "Token " + api_token
}

# Function to add text input to the chat log
def add_text(state, text):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=str(hackGPT_mode) + str(text),
        temperature=0,
        max_tokens=3000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n\n"]
    )
    response = response['choices'][0]['text']

    state += [(str(response), str(text))]

    try:
        with open('output/chat_hackGPT_log.csv', 'a+', encoding='UTF8', newline='') as f:
            w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            w.writerow([date_string, 'hackGPTv1', str(text).strip('\n'), str(response).lstrip('\n')])
    finally:
        return state

# Function to add file input to the chat log
def add_file(state, file):
    with open(file.name, 'r') as targets:
        search = targets.read()

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=str(search) + "\n",
        temperature=0,
        max_tokens=3000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\"\"\""]
    )

    file_response = response['choices'][0]['text']
    file_state = state + [("" + str(file_response), "Processed file: " + str(file.name)),]

    try:
        with open('output/chat_hackGPT_file_log.csv', 'a+', encoding='UTF8', newline='') as f:
            w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            w.writerow([date_string, 'hackGPTv1', str(search).strip('\n'), str(response).lstrip('\n')])
    finally:
        return state, file_state

# Define the hackchatGPT Gradio interface
with gr.Blocks(css="#chatbot .output::-webkit-scrollbar {display: none;}") as hackerchat:
    state = gr.State([])
    chatbot = gr.Chatbot().style(color_map=("black", "green"))

    with gr.Row():
        with gr.Column(scale=0.85):
            txt = gr.Textbox(show_label=False, placeholder="Enter query and press enter").style(container=False)
        with gr.Column(scale=0.15, min_width=0):
            btn = gr.UploadButton("ð", file_types=["file"])

    txt.submit(add_text, [state, txt], [chatbot, state])
    txt.submit(lambda: "", None, txt,)
    btn.upload(add_file, [state, btn], [state, state, chatbot])

if __name__ == "__main__":
    hackerchat.launch(height=1000, quiet=True, favicon_path="res/hackgpt_fav.png")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@title  Setting hackGPT Environment with OpenAI API key (Generate one here: https://platform.openai.com/account/api-keys )
#OpenAI API Setup
from dotenv import load_dotenv
import os
import fade
from pathlib import Path
import openai
from time import sleep
import os
import fade
from pathlib import Path
import openai
import requests
import urllib.parse
import urllib.request
import openai
from dotenv import load_dotenv
import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt
import json
import csv
import datetime
# Load API key from an environment variable or secret management service

load_dotenv(".env")
apiToken = os.environ.get('OPENAI_TOKEN')
openai.api_key = apiToken

if 'OPENAI_TOKEN' in os.environ:
   pass
else:
  error='''           
                     *   )           )            (   
                     `(     ( /((        (  (      )\   
                      )\(   )\())\  (    )\))(  ((((_) 
                     ((_)\ (_))((_) )\ ) ((   ))\  )\) 
                     8"""" 8"""8  8"""8  8"""88 8"""8  
                     8     8   8  8   8  8    8 8   8  
                     8eeee 8eee8e 8eee8e 8    8 8eee8e 
                     88    88   8 88   8 8    8 88   8 
                     88    88   8 88   8 8    8 88   8 
                     88eee 88   8 88   8 8eeee8 88   8 
                                  
   \033[1;33mAttempting to Set OpenAI system variable with API key.'''
  fadederror = fade.fire(error)
  print(fadederror)
  Path(".env").touch()
  setting_token = open(".env", "a")
  userkey = input('Enter OpenAI API Key: ').replace(" ","")
  setting_token.write("OPENAI_TOKEN="+'"'+userkey+'"\n')
def progress(percent=0, width=15):
    hashes = width * percent // 100
    blanks = width - hashes

    print('\r', hashes*'▒', blanks*' ', '', f' {percent:.0f}%', sep='',
        end='', flush=True)
print('𝙰𝚙𝚙𝚕𝚢𝚒𝚗𝚐 𝙰𝙿𝙸 𝚃𝚘𝚔𝚎𝚗')
for i in range(101):
    progress(i)
    sleep(.01)
print('\n')
print("𝙰𝙿𝙸 𝙲𝚘𝚗𝚏𝚒𝚐𝚞𝚛𝚊𝚝𝚒𝚘𝚗 𝚂𝚊𝚟𝚎𝚍 𝚝𝚘 .𝚎𝚗𝚟")    

#@title ChatBot and Web UI for HackGPT

hackGPT_mode = open('personas/hackGPTv1.md' ,"r")
hackGPT_mode = hackGPT_mode.read()
date_string = datetime.datetime.now()

load_dotenv()  
apiToken = os.environ.get("OPENAI_TOKEN")
headers = {
                    "Accept": "application/json; charset=utf-8",
                    "Authorization": "Token" + str(apiToken)
                }


if 'OPENAI_TOKEN' in os.environ:
    pass
else:
    os.environ['OPENAI_TOKEN'] = input('Enter API Key: ').replace(" ","")
token = os.environ.get("OPENAI_TOKEN")
hack=  "\n"*7 + r""" 



                          |¯¯¯¯| |¯¯¯¯| '/¯¯¯/.\¯¯¯\‚ '/¯¯¯¯/\¯¯¯¯\  |¯¯¯¯| |¯¯¯¯|
                          |:·.·|_|:·.·| |:·.·|_|:·.·| |:·.·|  |____| |:·.·|./____/ 
                          |:·.·|¯|:·.·| |:·.·|¯|:·.·| |:·.·|__|¯¯¯¯| |:·.·|.\¯¯¯¯\ 
                          |____| |____| |____|:|____|  \__ _\/____/  |____| |_____|
        
        
                                                                                  """ + "\n"*12

gpt = "\n"*4 +r""" 

                                                                                     ______  _______  ________ 
                                                                                   /      \|       \|        \
                                                                                   |  ▓▓▓▓▓▓\ ▓▓▓▓▓▓▓\\▓▓▓▓▓▓▓▓
                                                                                   | ▓▓ __\▓▓ ▓▓__/ ▓▓  | ▓▓   
                                                                                   | ▓▓|    \ ▓▓    ▓▓  | ▓▓   
 | ▓▓ \▓▓▓▓ ▓▓▓▓▓▓▓   | ▓▓   
| ▓▓__| ▓▓ ▓▓        | ▓▓   
 \▓▓    ▓▓ ▓▓        | ▓▓ 
  \▓▓▓▓▓▓ \▓▓         \▓▓
                      """                                                                                                 

fadedhack = fade.water(hack)
fadedgpt = fade.random(gpt)


for pair in zip(*map(str.splitlines, (fadedhack, fadedgpt))): 
  print(*pair)                                                                                                

#----------------------------------hackchatGPT---------------------------------------------------
with open('output/chat_hackGPT_log.csv', 'a+', encoding='UTF8', newline='') as f:
    w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    w.writerow(['Date', 'Persona', 'Query', 'Response'])
    f.close()
    
def add_text(state, text):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=str(hackGPT_mode) + str(text),
        temperature=0,
        max_tokens=3000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\"\"\""]
        )
    response = response['choices'][0]['text']
        
    state = state + [(str(response),str(text))]
    try:
        with open('output/chat_hackGPT_log.csv', 'a+', encoding='UTF8', newline='') as f:
            w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            w.writerow([date_string, 'hackGPTv1', str(text).strip('\n'), str(response).lstrip('\n')])
            f.close()
    finally:
        return state, state

def add_file(file_state, file):
    with open(file.name, 'r') as targets:
        search = targets.read()
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=str(search)+"\n",
            temperature=0,
            max_tokens=3000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["\"\"\""]
            )
        
    file_response = response['choices'][0]['text']
    file_state = file_state + [("" + str(file_response), "Processed file: "+ str(file.name))]
    try:
        with open('output/chat_hackGPT_file_log.csv', 'a+', encoding='UTF8', newline='') as f:
            w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            w.writerow([date_string, 'hackGPTv1', str(search).strip('\n'), str(response).lstrip('\n')])
            f.close()
    
    finally:
        return file_state, file_state
            


with gr.Blocks(css="#chatbot .output::-webkit-scrollbar {display: none;}") as hackerchat:
    state = gr.State([])
    chatbot = gr.Chatbot().style( color_map=("black", "green"))

    with gr.Row():
        with gr.Column(scale=0.85):
            txt = gr.Textbox(show_label=False, placeholder="Enter query and press enter").style(container=False)
        with gr.Column(scale=0.15, min_width=0):
            btn = gr.UploadButton("📁", file_types=["file"])

    txt.submit(add_text, [state, txt], [ chatbot, state])
    txt.submit(lambda :"", None, txt)
    btn.upload(add_file, [state, btn], [state, chatbot])
     
if __name__ == "__main__":
    hackerchat.launch(height=1000, quiet=True, favicon_path="res/hackgpt_fav.png")
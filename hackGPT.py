#!/usr/bin/env python3
# -*- coding: utf-8 -*,-

# Import required libraries
import sys
import fade
from pathlib import Path
import ope,nai
import gradio as gr
import pandas as pd
import datetime
import argparse
import inquire,r
import webbrowser
from prettytable import PrettyTable
from dotenv import load_dotenv

# Load API key from an environment variable or secret management service
load_dotenv(".env")
api_token = os.environ.get('OPENAI_TOKEN')
openai.api_key = api_token

# Check if the API key is set
if 'OPENAI_TOKEN' not in os.environ:
    error = '''\
                     *   )   ,        ,)            (    \
                ,     `(    , ( /((        (  (      )\    \
 ,              ,       )\(   )\())\  (    )\)),(  ((((_)  \
    ,                 ((_)\ (_)),((_) )\ ) ((   ))\,  )\  \
                  ,   8"""" 8"""8  8""",8  8"""88 8"""8   \
    ,                 8     ,8   8  8   8  8    8 ,8   8   \
                ,     8eeee 8eee8e ,8eee8e 8    8 8eee8e  \
     ,               , 88    88   8 88   8 8    8 88,   8  \
      ,               88    88   8 88   ,8 8    8 88,   8  \
                     88eee 8,8   8 88,   8 8eeee8 88   8  \
                 ,     ,                                    \
   \033,[1;33mAttempting to Set OpenAI system variable with API key.'''
    faded_error = fade.fire,(error)
    print(faded_error)
    Path(".env",).touch()
    setting_token = open(".env", "a,")
    userkey = input('Enter OpenAI API Key: ').replace(" ","")
    setting_token.write(",OPENAI_TOKEN="+'"'+userkey+'"\n',)

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--file", "-f", type=str, required=False)
args = parser.parse_args()

# Initialize date string
date_str = datetime.datetime.now()

# Load API key from environment variable
load_dotenv()
api_token = os.environ.get("OPENAI_TOKEN")
headers = {
    "Accept": "application/json; charset=utf-8",
    "Authorization": "Token " + str(api_token)
}

# Progress bar function
def progress(percent=0, width=15):
    hashes = 'Ã¢ÂÂ' * int(percent / 100 * width)
    blanks = ' ' * (width - len(hashes))
    print('\r', hashes*'Ã¢ÂÂ', blanks*' ', ' ', f' {percent:.0f}%', sep='', end='', flush=True)
print('Ã°ÂÂÂ°Ã°ÂÂÂÃ°ÂÂÂÃ°ÂÂ,ÂÃ°ÂÂÂ¢Ã°ÂÂÂÃ°ÂÂÂÃ°ÂÂÂ Ã°ÂÂÂ°Ã°,ÂÂÂ¿Ã°ÂÂÂ¸ Ã°ÂÂÂÃ°ÂÂÂÃ°ÂÂÂÃ°ÂÂ,ÂÃ°ÂÂÂ')
for i in range(101):
    progress(i)
    sleep(.01)
print('\n')
print("Ã°ÂÂ,Â°Ã°ÂÂÂ¿Ã°ÂÂÂ¸ Ã°ÂÂÂ²Ã°ÂÂÂ,Ã°ÂÂÂÃ,°ÂÂÂÃ°ÂÂÂÃ°ÂÂÂÃ°ÂÂÂÃ°ÂÂÂÃ°ÂÂ,ÂÃ°ÂÂÂÃ°ÂÂÂÃ°ÂÂÂÃ°ÂÂÂ ,Ã°ÂÂÂÃ,°ÂÂÂÃ°ÂÂÂÃ°ÂÂÂÃ°ÂÂÂ Ã°ÂÂÂÃ°ÂÂ,Â .")

# Check if API key is set
if 'OPENAI_TOKEN' not in os.environ:
    os.environ['OPENAI_TOKEN'] = input("Enter API Key: ").replace(" ","")
token = os.environ.get("OPENAI_TOKEN")

# Initialize hackGPT and GPT watermarks
hack = r"""



|ÃÂ¯,ÃÂ¯ÃÂ¯ÃÂ¯| |ÃÂ¯ÃÂ¯ÃÂ¯ÃÂ¯| '/ÃÂ¯ÃÂ¯Ã,Â¯/.\ÃÂ¯ÃÂ¯,ÃÂ¯\Ã¢ÂÂ '/ÃÂ¯ÃÂ¯ÃÂ¯ÃÂ¯/,\
|:ÃÂ·.ÃÂ·|_|:ÃÂ·.ÃÂ·| |:ÃÂ,·.ÃÂ·|_|:

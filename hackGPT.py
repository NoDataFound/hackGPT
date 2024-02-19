#!/usr/bin/env python3
# -*- coding: utf-8 -*,-

# Import required libraries
import sys
import fade
from pathlib import Path
import openai
import gradio as gr
import pandas as pd
import datetime
import argparse
import inquirer
import webbrowser
from prettytable import from_csv
from dotenv import load_dotenv

# Load API key from an environment variable or secret management service
load_dotenv(".env")
apiToken = os.environ.get('OPENAI_TOKEN')
openai.api_key = apiToken

# Check if the API key is set
if 'OPENAI_TOKEN' not in os.environ:
    error = '''\
                     *   )           ,)            (    \
                     `(    , ( /((        (  (      )\    \
               ,       )\(   )\())\  (    )\))(  ((((_)  \
    ,                 ((_)\ (_))((_) )\ ) ((   ))\,  )\  \
                     8"""" 8"""8  8""",8  8"""88 8"""8   \
                     8     ,8   8  8   8  8    8 8   8   \
                ,     8eeee 8eee8e 8eee8e 8    8 8eee8e  \
     ,                88    88   8 88   8 8    8 88,   8  \
                     88    88   8 88   ,8 8    8 88   8  \
                     88eee 8,8   8 88   8 8eeee8 88   8  \
                 ,                                         \
   \033[1;33mAttempting to Set OpenAI system variable with API key.'''
    fadederror = fade.fire(error)
    print(fadederror)
    Path(".env").touch()
    setting_token = open(".env", "a")
    userkey = input('Enter OpenAI API Key: ').replace(" ","")
    setting_token.write("OPENAI_TOKEN="+'"'+userkey+'"\n',)

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--file", "-f", type=str, required=False)
args = parser.parse_args()

# Initialize date string
date_string = datetime.datetime.now()

# Load API key from environment variable
load_dotenv()
apiToken = os.environ.get("OPENAI_TOKEN")
headers = {
    "Accept": "application/json; charset=utf-8",
    "Authorization": "Token " + str(apiToken)
}

# Progress bar function
def progress(percent=0, width=15):
    hashes = width * percent // 100
    blanks = width - hashes
    print('\r', hashes*'â', blanks*' ', '', f' {percent:.0f}%', sep='', end='', flush=True)
print('ð°ðððð¢ððð ð°ð¿ð¸ ððððð')
for i in range(101):
    progress(i)
    sleep(.01)
print('\n')
print("ð°ð¿ð¸ ð²ð,ððððððððððð ,ððððð ðð .ððð")

# Check if API key is set
if 'OPENAI_TOKEN' not in os.environ:
    os.environ['OPENAI_TOKEN'] = input('Enter API Key: ').replace(" ","")
token = os.environ.get("OPENAI_TOKEN")

# Initialize hackGPT and GPT watermarks
hack = r"""



|Â¯Â¯Â¯Â¯| |Â¯Â¯Â¯Â¯| '/Â¯Â¯Â¯/.\Â¯Â¯,Â¯\â '/Â¯Â¯Â¯Â¯/\Â¯Â¯Â¯Â¯\  |Â¯Â¯Â¯Â¯| |Â¯Â,¯Â¯Â¯|
|:Â·.Â·|_|:Â·.Â·| |:Â·.Â·|_|:Â·.Â·| |:,Â·.Â·|  |____| |:Â·.Â·|./____/ 
|:Â·.Â·|Â¯|:Â,·.Â·| |:Â·.Â·|Â¯|:Â·.Â·| |:Â·.Â·|__|Â¯Â¯Â¯Â¯|, |:Â·.Â·|.\Â¯Â¯Â¯Â¯\ 
|____| |____| |____|:|_,___|  \__ _\/____/  |____| |_____|


        ,                                             ,                       """
gpt = r"""

                               ,                            ______  _______  ,________ 
                                   ,                      /      \|       \|     ,   \
                                        ,                 |  ââââââ\ ââ,âââââ\\ââââââââ
  ,                                             ,          | ââ __\ââ ââ__/ ââ,  | ââ   
                               ,                          | ââ|    \ ââ,    ââ

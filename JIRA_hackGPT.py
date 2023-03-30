#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from dotenv import load_dotenv
import sys
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
import argparse
from prettytable.colortable import ColorTable, Themes
from prettytable import from_csv
from jira import JIRA
# Load API key from an environment variable or secret management service

load_dotenv(".env")
apiToken = os.environ.get('OPENAI_TOKEN')
jira_token = os.environ.get('JIRA_TOKEN')
openai.api_key = apiToken


if 'OPENAI_TOKEN' in os.environ:
    openai_token = os.environ['OPENAI_TOKEN']

elif 'JIRA_USER' in os.environ:

    jira_pass = os.environ['JIRA_TOKEN']
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
                                  
   \033[1;33mAttempting to Set OpenAI and JIRA system variable with API key.'''
  fadederror = fade.fire(error)
  print(fadederror)
  Path(".env").touch()
  setting_token = open(".env", "a")
  userkey = input('Enter OpenAI API Key: ').replace(" ","")
  setting_token.write("OPENAI_TOKEN="+'"'+userkey+'"\n')
  #https://id.atlassian.com/manage-profile/security/api-tokens
  jiratoken = input('Enter JIRA Token: ').replace(" ","")
  setting_token.write("JIRA_TOKEN="+'"'+jiratoken+'"\n')


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

# Authenticate with JIRA
#jira_url = input("Enter JIRA URL: ")
jira_options = {'server':  'YOUR_JIRA_URL'}
jira = JIRA(options=jira_options, basic_auth=('YOUR_JIRA_EMAIL', 'YOUR_JIRA_TOKEN'))


issues = jira.search_issues('type = bug ')
for issue in issues:
    ticket = fade.brazil("JIRA Ticket Summary: ")
    summary = fade.water(issue.fields.summary)
    description = fade.water(issue.fields.description)
    des_summary = fade.brazil("Issue description: ")
    print(ticket.rstrip('\n') + summary)
    print(des_summary.rstrip('\n'))
    print(description)
    prompt = f"Fix the following issue: {issue.fields.description}"
    model_engine = "davinci"
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    solution = fade.brazil("Genrating solution and adding to : ")
    print (solution)
    print("Sample: " + completions.choices[0].text[:40])
    response = completions.choices[0].text
    jira.add_comment(issue.key, response)

    #with open('output/JIRA_hackGPT_log.csv', 'a+', encoding='UTF8', newline='') as f:
    #    w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #    w.writerow([date_string,  {issue.fields.description}, str(response).lstrip('\n')])
    #    f.close()


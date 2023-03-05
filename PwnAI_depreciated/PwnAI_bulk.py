#Bulk OpenAI Search
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import fade
import json
import requests
import urllib.parse
import urllib.request
import argparse
import sys
import os
import shutil
from pathlib import Path
from os import path
from shutil import make_archive
from directory_structure import Tree
from alive_progress import alive_bar
from time import sleep
import openai
from dotenv import load_dotenv
load_dotenv()  
apiToken = os.environ.get("OPENAI_TOKEN")
#pwntxt= r"""
#                :                                                    :
#            ─ ──+──── ──  ─                                ─  ── ────+── ─
#               _|_____   __   __  ___  _____  ___        __        _.|     
#              |   __ "\ |"  |/  \|  "|(\"   \|"  \      /""\      |" \    
#              (. |__) :)|'  /    \:  ||.\\   \    |    /    \     ||  |   
#              |:  ____/ |: /'        ||: \.   \\  |   /' /\  \    |:  |   
#              (|  /      \//  /\'    ||.  \    \. |  //  __'  \   |.  |   
#             /|__/ \     /   /  \\   ||    \    \ | /   /  \\  \  /\  |\  
#            (_______)   |___/    \___| \___|\____\)(___/    \___)(__\_|_) 
#                |                                                    |
#            ─ ──+──── ──  ─                                ─  ── ────+── ─                                  
#                :                                                    :  
#╔─────────────────────────────-= OPEN API Notebook=-─────────────────── ¤ ◎ ¤ ──────╗
#║  ┌¤───────────────────────────────────┬────────────────────────Requirements───┐   ║ 
#╚──│  Format......: hax                 │  Payload..........: /input/           │───╝  
#   │  Date........: Nov 11,1999         │  API Token......: [********--] .env   │
#   ╚────────────────────────────────────┴───────────────────────────────────────╝"""
#fadedpwn = fade.purplepink(pwntxt)
#print(fadedpwn)
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
                                  
   \033[1;33mAttempting to Set OpenAI system variable with API key.

                      \033[0;37mExample: \033[40m$ 𝚎𝚡𝚙𝚘𝚛𝚝 OPENAI_TOKEN="𝙰𝙸 𝚃𝚘𝚔𝚎𝚗"
                      \033[0;37mSee sample \033[40m.𝚎𝚗𝚟\033[0;37m file for formating.'''


   fadederror = fade.fire(error)
   print(fadederror)
   Path(".env").touch()
   setting_token = open(".env", "a")
   userkey = input('Enter API Key: ').replace(" ","")
   setting_token.write("OPENAI_TOKEN="+'"'+userkey+'"')
   
targets = input("Enter Filename: (Press enter for 'input/sample_sources' ) ") or "input/sample_sources"
#investigation = input("Enter name for your investigation: ")

search = open(targets ,"r")
query = search.read()
fadedsearch =r"""
                                         
                  _____     _____          _____   ______         _____    ____ 
              ___|\    \   |\    \   _____|\    \ |\     \    ___|\    \  |    |
             |    |\    \  | |    | /    /|\\    \| \     \  /    /\    \ |    |
             |    | |    | \/     / |    || \|    \  \     ||    |  |    ||    |
             |    |/____/| /     /_  \   \/  |     \  |    ||    |__|    ||    |
             |    ||    |||     // \  \   \  |      \ |    ||    .--.    ||    |
             |    ||____|/|    |/   \ |    | |    |\ \|    ||    |  |    ||    |
             |____|       |\ ___/\   \|   /| |____||\_____/||____|  |____||____|
             |    |       | |   | \______/ | |    |/ \|   |||    |  |    ||    |
             |____|        \|___|/\ |    | | |____|   |___|/|____|  |____||____|
               \(             \(   \|____|/    \(       )/    \(      )/    \(  
                '              '      )/        '       '      '      '      '  
                                      '        
─ ──+──── ──  ─   ────────────────────────────────────────────────────────   ─  ── ────+── ─
 """ 
                                                     
tookewl=fade.purplepink(fadedsearch)
print(tookewl)

query_parse = json.dumps(query.split("\n"), sort_keys=True, indent=4)
print("\033[36msearching OpenAI for")
print(query_parse)
seperator = "─ ──+──── ──  ─   ────────────────────────────────────────────────────────   ─  ── ────+── ─"
faded_seperator = fade.water(seperator)
print(faded_seperator)
openai_targets = []

if 'OPENAI_TOKEN' in os.environ:
    pass
else:
    os.environ['OPENAI_TOKEN'] = input('Enter API Key: ').replace(" ","")
#f_jsonpath = 'output/'+investigation+'/results'
token = os.environ.get("OPENAI_TOKEN")

os.mkdir('output/'+investigation)
os.mkdir('output/'+investigation+'/results/')

with open(targets, 'r') as targets:
    for line in targets:
        openai_targets.append(line)
        
    
    for search in openai_targets:
        #search = search.strip()
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=search+"\n\n",
        temperature=0,
        max_tokens=64,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\"\"\""]
        )
        response = response['choices'][0]['text']
        #with open('output/'+investigation+'/results/'+str(search.rsplit('/', 1)[-1])+ ".txt", "w") as f:
        #    f.write(response)
        fadedresponse = fade.greenblue(response)

        print(' '*39+"🆁🅴🆂🆄🅻🆃🆂\n" + "𝘚𝘦𝘢𝘳𝘤𝘩 𝘴𝘰𝘶𝘳𝘤𝘦 𝘪𝘯𝘱𝘶𝘵:"+ str(search).strip())
        print("\n\033[36mHere's your code:")
        sleep(5)
        print(fadedresponse)
        print(faded_seperator)
        


#path = Tree(f_jsonpath, absolute=False)
print(path)

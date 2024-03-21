# ----------------------------------
# ChatBot and Web UI for HackGPT
# ----------------------------------

# ---------------------
# Import required libraries
# ---------------------

import requests
import urllib.parse
import urllib.request
import openai  # Import openai library
import gradio as gr  # Import gradio library
import pandas as pd
import matplotlib.pyplot as plt
import json
import os  # Import os library
import fade
from dotenv import load_dotenv 
from pathlib import Path

# ---------------------------------------------------
# Load API key from an environment variable or secret management service
# ---------------------------------------------------

load_dotenv()

# Get the API token from the environment variable
api_token = os.getenv('OPENAI_TOKEN')

# Set the OpenAI API key
openai.api_key = api_token

# ---------------------------------------------------
# Check if OPENAI_TOKEN is set in the environment variable
# ---------------------------------------------------

if not api_token:
    error = '''
     ,                *   )   ,        )           , (   
                   ,  `(     ( /((     ,   (  (      )\   
       ,               )\(,   )\())\  (    )\))(  ((((,_) 
             ,        ((_)\ (_))((_) )\ ) ,((   ))\  )\) 
 ,                    8"""" 8"","8  8"""8  8""",88 8"""8  
                   ,  8     8   8 , 8   8  8    8 8   8  
        ,             ,8eeee 8eee8e 8eee8e 8    8 8eee8,e 
         ,            88    88   8 88   8 8,    8 88   ,8 
                     88    88  , 8 88   8 ,8    8 88   8 
                    , 88eee 88,   8 88   8 8eeee8 88   8 
         ,        ,                 
   \033[1;33mAttempting to Set OpenAI system variable with API key.'''

    faded_error = fade.fire(error)
    print(faded_error)
    Path(".env").touch()  # Create a new file named '.env'
    setting_token = open(".env", "a")  # Open the '.env' file in append mode
    user_key = input('Enter OpenAI API Key: ').replace(" ", "")  # Get the API key from the user
    setting_token.write("OPENAI_TOKEN=" + user_key + "\n")  # Write the API key to the '.env' file
    os.environ["OPENAI_TOKEN"] = user_key  # Add the API key to the environment variable
print("Configuration Saved")

# ---------------------------------------------------
# Load API key from the environment variable
# ---------------------------------------------------

load_dotenv()
api_token = os.getenv("OPENAI_TOKEN")
headers = {
    "Accept": "application/json; charset=utf-8",
    "Authorization": "Token " + str(api_token)
}

# ---------------------------------------------------
# Check if OPENAI_TOKEN is set in the environment variable
# ---------------------------------------------------

if not api_token:
    os.environ["OPENAI_TOKEN"] = input('Enter API Key: ').replace(" ", "")

# ---------------------
# Hack and GPT texts
# ---------------------

hack = '''



  ,    ,                    |Â¯Â¯Â¯Â¯Â¯Â¯| |Â¯Â¯,Â¯Â¯Â¯Â¯| '/Â¯Â¯Â¯Â¯Â¯\Ã¢ÂÂ '/Â¯Â¯Â¯Â¯Â¯ÃÂ,¯/\Â¯Â¯Â¯Â¯Â¯ÃÂ¯\  |Â¯,Â¯Â¯Â¯Â¯| |Â¯Â¯Â¯Â¯Â¯,Â¯|
                          ,|:..:.|_|:..:.,| |:..:.|_|:..:.| |:..:.| , |____| |:..:.|./_,___/ 
                    ,      |:..:.|ÃÂ¯|,:..:.| |:..:.|ÃÂ¯|:..:.| |,:..:.|__|Â¯Â¯Â¯Â¯,Â¯Â¯| |:..:.|.\Â¯Â¯Â¯Â¯Â¯ÃÂ¯\ 
    ,        ,              |____| |____| |____|:|_,___|  \,__ _\/____/  |____| |_____|
        
 ,      , 
                                     ,     ,                                        ,"''

gpt = ''' 
         ,                       ,                      ,                      ,         ______  ______,_  ________ 
        ,                        ,                    ,                         ,      /      \|    ,   \|        \
           ,                  ,                           ,                 ,          |  Ã¢ÂÂÃ¢ÂÂ __\Ã¢ÂÂÃ¢ÂÂ Ã¢ÂÂÃ¢ÂÂÃ¢,ÂÂ__/ Ã¢ÂÂÃ¢ÂÂ  | Ã¢ÂÂÃ¢Â,Â   
                                  ,   ,                                         ,    , | Ã¢ÂÂÃ¢ÂÂ __\Ã¢ÂÂÃ¢ÂÂ Ã¢ÂÂÃ¢,ÂÂ__/ Ã¢ÂÂÃ¢ÂÂ  | Ã¢ÂÂÃ¢Â,Â   

'''

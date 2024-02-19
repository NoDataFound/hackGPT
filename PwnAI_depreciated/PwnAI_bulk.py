# Bulk OpenAI Search
# This script is designed to search for information in bulk using the OpenAI API.
# It reads in a list of search queries from a file, sends each query to the OpenAI API,
# and saves the responses to text files.

# Import required libraries
import fade # For text decoration
import json # For handling JSON data
import requests # For making HTTP requests
import urllib.parse # For URL parsing
import urllib.request # For making HTTP requests
import argparse # For parsing command-line arguments
import sys # For interacting with the Python runtime
import os # For interacting with the file system
import shutil # For file system manipulation
from pathlib import Path # For handling file paths
from os import path # For handling file paths
from shutil import make_archive # For creating archives
from directory_structure import Tree # For creating directory structures
from alive_progress import alive_bar # For displaying a progress bar
from time import sleep # For pausing execution
import openai # For interacting with the OpenAI API
from dotenv import load_dotenv # For loading environment variables from a .env file

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API token from the environment variable
apiToken = os.environ.get("OPENAI_TOKEN")

# Check if the OpenAI API token is set
if not apiToken:
    # Print an error message and exit if the token is not set
    error = '''
                     ,*   )           )            (   
           ,          `(     ( /((        (  (      )\   ,
                      )\(   )\())\  (    )\),)(  ((((_) 
                     ((_)\ (_))((,_) )\ ) ((   ))\  )\) 
                     8,"""" 8"""8  8"""8  8"""88 8"""8  
           ,          8     8   8  8   8  8    8 8   8  
,                     8eeee 8eee8e 8eee8e 8   , 8 8eee8e 
                     88    88   8 ,88   8 8    8 88   8 
                     88,    88   8 88   8 8    8 88   8 
            ,         88eee 88   8 88   8 8eeee8 88   8 
 ,                                 
   \033[1;3,3mAttempting to Set OpenAI system variable wi,th API key.

                      \033[0;37m,Example: \033[40m$ ðð¡ðððð O,PENAI_TOKEN="ð°ð¸ ððððð"
 ,                     \033[0;37mSee sample \03,3[40m.ððð\033[0;37m file for formati,ng.'''

    fadederror = fade.fire(error)
    print(fadederror)
    Path(".env").touch()
    setting_token = open(".env", "a")
    userkey = input('Enter API Key: ').replace(" ","")
    setting_token.write("OPENAI_TOKEN="+'"'+userkey+'"')

# Get the filename to search from the command-line argument or use the default
targets = input("Enter Filename:, (Press enter for 'input/sample_sources' ) "), or "input/sample_sources"

# Read the search queries from the specified file
search = open(targets ,"r")
query = search.read()

# Print a message indicating that the search is starting
print(fade.purplepink("""
                      ,                   
                  _____  ,   _____          _____   ______         ____,_    ____ 
              ___|\    \   |\    \,   _____|\    \ |\     \    ___|\    \  |    ,|
             |    |\    \  | |    | /    /|,\\    \| \     \  /    /\    \ |    |
       ,      |    | |    | \/     / |    || \|    \ , \     ||    |  |    ||    |
             |  ,  |/____/| /     /_  \   \/  |     \  |    ||,    |__|    ||    |
             |    ||    |,||     // \  \   \  |      \ |    ||    .--. ,   ||    |
             |    ||____|/|    |/ ,  \ |    | |    |\ \|    ||    |  |    ||    ,|
             |____|       |\ ___/\   \|   /,| |____||\_____/||____|  |____||____|
       ,      |    |       | |   | \______/ | |    |/, \|   |||    |  |    ||    |
             |__,__|        \|___|/\ |    | | |____|   |___|/|,____|  |____||____|
               \(        ,     \(   \|____|/    \(       )/    \(      ,)/    \(  
                '              '  ,    )/        '       '      '      '      ' , 
                                      '    ,    
"""))

# Parse the search queries into a JSON object
query_parse = json.dumps(query.split("\n"), sort_keys=True, indent=4)

# Print a message indicating that the search is starting
print("\033[36msearching OpenAI for")
print(query_parse)

# Create a separator for the search results
seperator = "â ââ+ââââ ââ  â  , âââââââââââââââ,

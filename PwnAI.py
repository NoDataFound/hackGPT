import fade
from dotenv import load_dotenv
import os
from pathlib import Path
import openai
pwntxt= r"""
                :                                                    :
            ─ ──+──── ──  ─                                ─  ── ────+── ─
               _|_____   __   __  ___  _____  ___        __        _.|     
              |   __ "\ |"  |/  \|  "|(\"   \|"  \      /""\      |" \    
              (. |__) :)|'  /    \:  ||.\\   \    |    /    \     ||  |   
              |:  ____/ |: /'        ||: \.   \\  |   /' /\  \    |:  |   
              (|  /      \//  /\'    ||.  \    \. |  //  __'  \   |.  |   
             /|__/ \     /   /  \\   ||    \    \ | /   /  \\  \  /\  |\  
            (_______)   |___/    \___| \___|\____\)(___/    \___)(__\_|_) 
                |                                                    |
            ─ ──+──── ──  ─                                ─  ── ────+── ─                                  
                :                                                    :  
╔─────────────────────────────-= OPEN API Notebook=-─────────────────── ¤ ◎ ¤ ──────╗
║  ┌¤───────────────────────────────────┬────────────────────────Requirements───┐   ║ 
╚──│  Format......: hax                 │  Payload..........: /input/           │───╝  
   │  Date........: Nov 11,1999         │  API Token......: [********--] .env   │
   ╚────────────────────────────────────┴───────────────────────────────────────╝"""
fadedpwn = fade.purplepink(pwntxt)
print(fadedpwn)

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
                                  
   \033[1;33mAttempting to Set OpenAI system variable with API key.

                      \033[0;37mExample: \033[40m$ 𝚎𝚡𝚙𝚘𝚛𝚝 OPENAI_TOKEN="𝙰𝙸 𝚃𝚘𝚔𝚎𝚗"
                      \033[0;37mSee sample \033[40m.𝚎𝚗𝚟\033[0;37m file for formating.'''


   fadederror = fade.fire(error)
   print(fadederror)
   Path(".env").touch()
   setting_token = open(".env", "a")
   userkey = input('Enter API Key: ').replace(" ","")
   setting_token.write("OPENAI_TOKEN="+'"'+userkey+'"')
   
#Single Lookups
payload = input("Enter Filename: (Press enter for 'input/malware/malware_sample' ) ") or "input/malware/malware_sample"
payload = open(payload, "r").readlines()
payload = str(payload)
response = openai.Completion.create(
  model="code-davinci-002",
  prompt=payload+"\nHere's what this malware is doing:\n1.",
  temperature=0,
  max_tokens=64,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=["\"\"\""]
)
response = response['choices'][0]['text']
fadedresponse = fade.greenblue(response)
print(fadedresponse)           
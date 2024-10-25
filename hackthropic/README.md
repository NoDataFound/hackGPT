
# [DEPREICATED] Moved to new org https://github.com/haKC-ai/hakcthropic/

![Python 3.11](https://img.shields.io/badge/Python-3.11-blue)
![Docker](https://img.shields.io/badge/Docker-Required-green)
![GitHub last commit](https://img.shields.io/github/last-commit/anthropics/anthropic-quickstarts)

`[DEPREICATED] Moved to new org https://github.com/haKC-ai/hakcthropic/`

This repo just aims to get you started with Anthropics Quickstarts environment to deploy "AI" hacking agents for shenanigans.  
<img width="1921" alt="Screenshot 2024-10-23 at 9 04 38 PM" src="https://github.com/user-attachments/assets/d110e3fd-c401-49c8-9836-2d6d195f5c2a">

Why: On Oct 22, 2024 [Anthropic released ](https://www.anthropic.com/news/3-5-models-and-computer-use) and in part it states:

*"We’re also introducing a groundbreaking new capability in public beta: computer use. Available today on the API, developers can direct Claude to use computers the way people do—by looking at a screen, moving a cursor, clicking buttons, and typing text. Claude 3.5 Sonnet is the first frontier AI model to offer computer use in public beta."*

So in this repo, I am showing how the install guide leverages this to install metasploit, set options and execute an attack.

[DEPREICATED] Moved to new org https://github.com/haKC-ai/hakcthropic/

https://github.com/user-attachments/assets/4f6b5827-89d0-47d9-ace3-2d0965f5358b

## Curious Notes

- on the VM in as the user home dir, there is a hidden directory called `~/.anthropic/` which I found two files:
    - `api_key`
    - `system_prompt`
   
        - The default state of the system prompt is blank, I had decent luck giving it instructions similar to "jailbreaks".
        - Documentation for this is here: https://docs.anthropic.com/en/docs/build-with-claude/computer-use
            - I had pretty good luck with it respecting these prompts prior to running the commands issues in the streamlit input field   
            - <img width="784" alt="Screenshot 2024-10-24 at 9 26 43 AM" src="https://github.com/user-attachments/assets/bcc307c9-c1d7-4719-a6b3-1b62a69a5ec2">
           Interesting note: Even though its getting instruction to not intereact with external resources, it clearly ignores them.
          ya know.. since I was able to clone MSF and run it against something externally.
          
          ![8yalrx](https://github.com/user-attachments/assets/f51f6fd1-15b0-4a95-b685-55376687dc25)

- I experienced this issue ["Claude sometimes assumes outcomes of its actions without explicitly checking their results. "](https://docs.anthropic.com/en/docs/build-with-claude/computer-use) with some of my commands dispite telling it:

  ```... Run each command one at a time and make sure they complete.  I want to see the output as you run the command.```
  [DEPREICATED] Moved to new org https://github.com/haKC-ai/hakcthropic/
## Prerequisites

- [Read the docs](https://docs.anthropic.com/en/docs/build-with-claude/computer-use)
- Get your Anthropic API key from the [console](https://console.anthropic.com/dashboard)


## Setup Instructions

1. Clone this repository:
    ```bash
    git clone https://github.com/anthropics/anthropic-quickstarts.git
    #Then download my start_hacking.sh script here: https://github.com/NoDataFound/hackGPT/tree/main/hackthropic or just clone this entire repo
    git clone https://github.com/NoDataFound/hackGPT.git
    ```
    
2. Run the `start_hacking.sh` script: 
    ```bash
    hackGPT/hackthropic/start_hacking.sh #or whereever you saved it
    ```

## Environment Variables

Add your `ANTHROPIC_API_KEY API key to `.env`  ` 

Format of the `.env` file:
```
ANTHROPIC_API_KEY=<your_api_key>
```

## Usage

The `start_hacking.sh` script will:
1. Create a Python virtual environment.
2. Install the required dependencies.
3. Export environment variables from the `.env` file.
4. Run the Docker container with appropriate port bindings and environment variables.

## Notes

- Ensure Docker is installed and running on your system.
- The script drops the `.env` file in `anthropic-quickstarts/computer-use-demo/`.



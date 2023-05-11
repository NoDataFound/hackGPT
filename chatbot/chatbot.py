import os
import openai
import json
from dotenv import load_dotenv, set_key
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack import WebClient
from slack_bolt import App

load_dotenv('.env')
openai.api_key = os.environ.get('OPENAI_API_KEY')
slack_bot_token = os.environ.get('SLACK_BOT_TOKEN')
slack_app_token = os.environ.get('SLACK_APP_TOKEN')

if not openai.api_key:
    openai.api_key = input("Enter OPENAI_API_KEY API key")
    set_key('.env', 'OPENAI_API_KEY', openai.api_key)

if not slack_bot_token:
    slack_bot_token = input("Enter SLACK_BOT_TOKEN")
    set_key('.env', 'SLACK_BOT_TOKEN', slack_bot_token)

if not slack_app_token:
    slack_app_token = input("Enter SLACK_APP_TOKEN")
    set_key('.env', 'SLACK_APP_TOKEN', slack_app_token)

os.environ['SLACK_BOT_TOKEN'] = slack_bot_token
os.environ['SLACK_APP_TOKEN'] = slack_app_token
os.environ['OPENAI_API_KEY'] = openai.api_key

app = App(token=slack_bot_token)
client = WebClient(slack_bot_token)

def get_persona_dropdown():
    persona_options = []
    personas = [f for f in os.listdir("personas") if os.path.isfile(os.path.join("personas", f))]
    for persona in personas:
        persona_filename = "personas/" + persona
        with open(persona_filename, "r") as f:
            persona_text = f.read()
        persona_name = persona.split('.')[0]
        persona_options.append({"label": persona_name, "value": persona_text})
    return persona_options

hackGPTv1 = "personas/hackGPTv1.md"
Linux_Terminal_remote = "personas/Linux_Terminal_remote.md"
ThreatHunter = "personas/ThreatHunter.md"

with open(hackGPTv1, "r") as f:
    hackGPTv1_text = f.read()

with open(Linux_Terminal_remote, "r") as f:
    linux_text = f.read()

with open(ThreatHunter, "r") as f:
    threathunter_text = f.read()

@app.event("app_mention")
def handle_message_events(ack, body, logger):
    prompt = str(body["event"]["text"]).split(">")[1]

    response = client.chat_postMessage(
        channel=body["event"]["channel"],
        thread_ts=body["event"]["event_ts"],
        text=f":hackgpt: processing..."
    )

    if "persona" in prompt.lower().split():
        blocks = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Pick a persona from the dropdown list"
                },
                "accessory": {
                    "type": "static_select",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Personas",
                        "emoji": True
                    },
                    "options": [
                        {
                            "text": {
                                "type": "plain_text",
                                "text": ":hackgpt: *hackGPTv1*",
                                "emoji": True
                            },
                            "value": hackGPTv1_text
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": ":terminal: *Linux Terminal*",
                                                                "emoji": True
                            },
                            "value": linux_text
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": ":pirate_flag: *ThreatHunter*",
                                "emoji": True
                            },
                            "value": threathunter_text
                        }
                    ],
                    "action_id": "static_select-action"
                }
            }
        ]

        response = client.chat_postMessage(
            channel=body["event"]["channel"],
            thread_ts=body["event"]["event_ts"],
            blocks=blocks,
            text="Pick a persona from the dropdown list"
        )
    else:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=1.0
        ).choices[0].text

        response = client.chat_postMessage(
            channel=body["event"]["channel"],
            thread_ts=body["event"]["event_ts"],
            text=f"Here you go: \n{response}"
        )

@app.action("static_select-action")
def handle_static_select_action(ack, body, logger):
    ack()
    selected_option_value = body["actions"][0]["selected_option"]["value"]
    message_text = body["message"]["text"]
    prompt_start_index = message_text.find(":") + 1
    prompt = message_text[prompt_start_index:].strip()
    prompt_with_persona = selected_option_value + prompt

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt_with_persona,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=1.0
    ).choices[0].text

    response = client.chat_postMessage(
        channel=body["channel"]["id"],
        thread_ts=body["message"]["thread_ts"],
        text=f"Here you go:\n{response}"
    )


if __name__ == "__main__":
    SocketModeHandler(app, slack_app_token).start()


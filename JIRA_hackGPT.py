#!/usr/bin/env python3
# -*- coding: utf-8 -*,-  Encoding declaration for non-ASCII characters

import os
import fade  # Unknown import, possibly custom or unnecessary
import requests
import urllib.parse as urlparse  # Parse URLs
import urllib.request as urlrequest  # Make HTTP requests
import openai  # Interact with OpenAI API
import pandas as pd  # Data manipulation and analysis
import matplotlib.pyplot as plt  # Data visualization
import json  # Work with JSON data
import csv  # Work with CSV files
import datetime as dt  # Date and time manipulation
import argparse  # Command line argument parsing

from prettytable import from_csv, ColorTable, Themes  # Data display
from jira import JIRA  # Interact with JIRA

# Load API key from environment variable or secret management service
load_dotenv(".env")
api_token = os.getenv("OPENAI_TOKEN")
jira_token = os.getenv("JIRA_TOKEN")
openai.api_key = api_token

# Authenticate with JIRA
jira_options = {'server': 'YOUR_JIRA_URL'}
jira = JIRA(options=jira_options, basic_auth=('YOUR_JIRA_EMAIL', jira_token))

# Fetch all open bugs from JIRA
issues = jira.search_issues('type = bug')

# Iterate through each issue
for issue in issues:
    # Print JIRA ticket summary
    ticket = f"JIRA Ticket Summary: {issue.fields.summary}"
    print(fade.water(ticket))

    # Print issue description
    description = fade.water(issue.fields.description)
    print(fade.water(description))

    # Generate a prompt for the issue
    prompt = f"Fix the following issue: {issue.fields.description}"

    # Set the OpenAI model engine
    model_engine = "davinci"

    # Generate a solution using OpenAI
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Print the generated solution
    solution = fade.brazil("Generating solution and adding to JIRA: ")
    print(fade.brazil(solution))
    print("Sample: " + completions.choices[0].text[:40])

    # Add the solution as a comment to the JIRA issue
    response = completions.choices[0].text
    jira.add_comment(issue.key, response)

    # Log the issue and solution to a CSV file
    # with open('output/JIRA_hackGPT_log.csv', 'a+', encoding='UTF8', newline='') as f:
    #     w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #     w.writerow([dt.datetime.now(), issue.fields.description, response])

import json
import requests
import argparse
import os
import shutil
from pathlib import Path
from tqdm import tqdm
import openai

def read_queries(file):
    with open(file, "r") as search:
        queries = search.readlines()
    return queries

def search(queries, api_key):
    openai.api_key = api_key
    responses = []
    for query in tqdm(queries):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=query,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        responses.append(response.choices[0].text)
    return responses

def save_responses(responses, file):
    with open(file, "w") as output:
        for response in responses:
            output.write(response + "\n")

def main():
    parser = argparse.ArgumentParser(description="Bulk OpenAI Search")
    parser.add_argument("file", help="The filename to search")
    parser.add_argument("-t", "--token", help="The OpenAI API token")
    args = parser.parse_args()

    if args.token:
        api_key = args.token
    else:
        api_key = os.environ.get("OPENAI_TOKEN")

    if not api_key:
        print("Error: OpenAI API token not set")
        sys.exit(1)

    queries = read_queries(args.file)
    responses = search(queries, api_key)
    save_responses(responses, f"{Path(args.file).with_suffix('.txt')}")

if __name__ == "__main__":
    main()


python bulk_openai_search.py <filename> -t <api_token>

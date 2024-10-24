
# Hackthropic Quickstart

![Python 3.11](https://img.shields.io/badge/Python-3.11-blue)
![Docker](https://img.shields.io/badge/Docker-Required-green)
![GitHub last commit](https://img.shields.io/github/last-commit/anthropics/anthropic-quickstarts)

This repo just aims to get you started with Anthropics Quickstarts environment to deploy "AI" hacking agents for shenanigans.  

Why: On Oct 22, 2024 [Anthropic released ](https://www.anthropic.com/news/3-5-models-and-computer-use) and in part it states:

*"We’re also introducing a groundbreaking new capability in public beta: computer use. Available today on the API, developers can direct Claude to use computers the way people do—by looking at a screen, moving a cursor, clicking buttons, and typing text. Claude 3.5 Sonnet is the first frontier AI model to offer computer use in public beta."*

## Prerequisites

- [Read the docs](https://docs.anthropic.com/en/docs/build-with-claude/computer-use)
- Get your Anthropic API key from the [console](https://console.anthropic.com/dashboard)


## Setup Instructions

1. Clone this repository:
    ```bash
    git clone https://github.com/anthropics/anthropic-quickstarts.git
    ```
2. Run the `start_hacking.sh` script: 
    ```bash
    ./start_hacking.sh
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



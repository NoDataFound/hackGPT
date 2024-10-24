
#!/bin/bash

git clone https://github.com/anthropics/anthropic-quickstarts.git

echo "ANTHROPIC_API_KEY=" > anthropic-quickstarts/computer-use-demo/.env

python3.11 -m venv haKC
source haKC/bin/activate
haKC/bin/python -m pip install --upgrade -q pip
haKC/bin/python -m pip install -q -r anthropic-quickstarts/computer-use-demo/dev-requirements.txt

# Check if .env file exists and export variables
if [ -f anthropic-quickstarts/computer-use-demo/.env ]; then
    export $(cat anthropic-quickstarts/computer-use-demo/.env | grep -v '^#' | xargs)
else
    echo "Error: .env file not found"
    exit 1
fi

if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "Error: ANTHROPIC_API_KEY not found in .env file"
    exit 1
fi

cd anthropic-quickstarts/computer-use-demo/

docker run \
    -e ANTHROPIC_API_KEY="$ANTHROPIC_API_KEY" \
    -v $HOME/.anthropic:/home/computeruse/.anthropic \
    -p 5900:5900 \
    -p 8501:8501 \
    -p 6080:6080 \
    -p 8080:8080 \
    -e WIDTH=600 \
    -e HEIGHT=800 \
    -it ghcr.io/anthropics/anthropic-quickstarts:computer-use-demo-latest

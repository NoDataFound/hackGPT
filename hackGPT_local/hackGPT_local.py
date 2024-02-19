import streamlit as st
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, T5ForConditionalGeneration, BartForConditionalGeneration

# Function to download the webpage and extract text
def download_webpage(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc.split(".")[0]
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")
    text_content = soup.get_text(separator=" ")
    return text_content

# Set page configuration
st.set_page_config(page_title="ððððð»ð¾ð¥", page_icon="https://raw.githubusercontent.com/NoDataFound/hackGPT/main/res/hackgpt_fav.png", layout="wide")

# Display app logo and title
st.image("https://raw.githubusercontent.com/NoDataFound/hackGPT/main/res/hackGPT_logo.png", width=80)
st.sidebar.markdown("""
    <center>
        <img src='https://raw.githubusercontent.com/NoDataFound/hackGPT/main/res/hackgpt_fav.png' alt='hackGPTlogo' width='64'/> 
        hackGP<T> with Local LLMS
    </center>
""", unsafe_allow_html=True)
st.sidebar.markdown("----")

# Model information
model_info = {
    "BERT": {
        "description": "BERT (Bidirectional Encoder Representations from Transformers), is a transformer-based model that has achieved state-of-the-art performance on various NL tasks.",
        "website": "https://huggingface.co/transformers/model_doc/bert.html",
    },
    # ... other models omitted for brevity
}

# Models
models = {
    "BERT": "bert-large-uncased-whole-word-masking-finetuned-squad",
    # ... other models omitted for brevity
}

# Metrics
num_models = len(models)
num_urls_entered = 0
model_counts = {model_name: 0 for model_name in models}

# Function to download the webpage and extract text
def download_webpage(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc.split(".")[0]
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")
    text_content = soup.get_text(separator=" ")
    return text_content

# Function to display model information
def display_model_info(model_name):
    info = model_info[model_name]
    st.write(f"**Description:** {info['description']}")
    st.write(f"**Website:** [{model_name}]({info['website']})")

# Model selection
selected_model = st.sidebar.selectbox("Select Model", list(model_info.keys()))

# Model loading
tokenizer = AutoTokenizer.from_pretrained(models[selected_model])
model = AutoModelForQuestionAnswering.from_pretrained(models[selected_model])

# Metrics
num_models = len(model_info)
num_urls_entered = 0
model_counts = {model_name: 0 for model_name in models}

# Streamlit app
st.title("Document Question Answering")

# Display model information
st.markdown("----")
display_model_info(selected_model)
st.markdown("----")

# User input
url = st.sidebar.text_input("Enter a URL")
uploaded_file = st.sidebar.file_uploader("Upload a document")
question = st.text_input("Enter your question", key="question")

# Process user input and perform question answering
if question:
    text_content = ""
    if url:
        text_content = download_webpage(url)
        st.write("Webpage downloaded successfully.")
    elif uploaded_file is not None:
        text_content = uploaded_file.read().decode("utf-8")
        st.write("File uploaded successfully.")
    else:
        st.warning("Please upload a document or enter a URL.")

    if text_content and question:
        # Split the document into chunks of fixed length
        max_chunk_length = 512
        document_chunks = [text_content[i:i + max_chunk_length] for i in range(0, len(text_content), max_chunk_length)]

        # Answer each chunk separately
        answers = []
        for chunk in document_chunks:
            inputs = tokenizer.encode_plus(question, chunk, max_length=512, truncation=True, return_tensors="pt")
            answer = model(**inputs).last_hidden_state[:, 0, :]
            answer = answer.tolist()[0]
            answers.append(answer)

        # Combine answers from different chunks
        answer = " ".join([str(i) for i in answers])

        st.write("Answer:")
        st.write(answer)

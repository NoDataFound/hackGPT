import streamlit as st
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from transformers import AutoTokenizer, AutoModelForQuestionAnswering, T5Tokenizer, T5ForConditionalGeneration, BartTokenizer, BartForConditionalGeneration
from transformers import (
    AutoConfig,
    AutoModelForSeq2SeqLM,
    AutoTokenizer,
    DataCollatorForSeq2Seq,
    HfArgumentParser,
    MBart50Tokenizer,
    MBart50TokenizerFast,
    MBartTokenizer,
    MBartTokenizerFast,
    Seq2SeqTrainer,
    Seq2SeqTrainingArguments,
    set_seed,
)
import pandas as pd
import torch
# Create a function to download the webpage and extract text
def download_webpage(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc.split(".")[0]
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")
    text_content = soup.get_text(separator=" ")
    return text_content

st.set_page_config(page_title="𝚑𝚊𝚌𝚔🅶🅿🆃", page_icon="https://raw.githubusercontent.com/NoDataFound/hackGPT/main/res/hackgpt_fav.png", layout="wide")
st.image('https://raw.githubusercontent.com/NoDataFound/hackGPT/main/res/hackGPT_logo.png', width=800)

st.sidebar.markdown("""
    <center>

    <img src='https://raw.githubusercontent.com/NoDataFound/hackGPT/main/res/hackgpt_fav.png' alt='hackGPTlogo' width='64'/> 
 
    hackGPT with Local LLMS

    </center>
""", unsafe_allow_html=True)
st.sidebar.markdown("----")
# Model information
model_info = {
    "BERT": {
        "description": "BERT (Bidirectional Encoder Representations from Transformers) is a transformer-based model that has achieved state-of-the-art performance on various NLP tasks.",
        "website": "https://huggingface.co/transformers/model_doc/bert.html",
    },
    "DistilBERT": {
        "description": "DistilBERT is a distilled version of BERT that retains most of its performance while being faster and requiring less memory.",
        "website": "https://huggingface.co/transformers/model_doc/distilbert.html",
    },
    "RoBERTa": {
        "description": "RoBERTa (Robustly Optimized BERT Pretraining Approach) is another variant of BERT that has achieved state-of-the-art results on a range of NLP tasks.",
        "website": "https://huggingface.co/transformers/model_doc/roberta.html",
    },
    "ALBERT": {
        "description": "ALBERT (A Lite BERT) is a lightweight version of BERT that reduces the memory footprint while maintaining competitive performance.",
        "website": "https://huggingface.co/transformers/model_doc/albert.html",
    },
    "Electra": {
        "description": "Electra is a model that uses a generator-discriminator architecture for pretraining, resulting in improved efficiency and performance.",
        "website": "https://huggingface.co/transformers/model_doc/electra.html",
    },
    "XLNet": {
        "description": "XLNet is an autoregressive pretraining method that incorporates permutation-based training and relative positional encoding. It achieves state-of-the-art results on various NLP tasks.",
        "website": "https://huggingface.co/transformers/model_doc/xlnet.html",
    },
    "Longformer": {
        "description": "Longformer is a transformer-based model that can process documents of up to 4096 tokens in length. It has been fine-tuned on the TriviaQA dataset for question answering.",
        "website": "https://huggingface.co/transformers/model_doc/longformer.html",
    },
    "SpanBERT": {
        "description": "SpanBERT is a model that incorporates a span-based objective to better represent the meaning of sentences. It achieves state-of-the-art performance on various NLP tasks.",
        "website": "https://huggingface.co/transformers/model_doc/spanbert.html",
    },
    "T5": {
        "description": "T5 (Text-To-Text Transfer Transformer) is a model that can be trained in a wide range of tasks by using a unified text-to-text format. It has been fine-tuned on the SQuAD dataset for question answering.",
        "website": "https://huggingface.co/transformers/model_doc/t5.html",
    },
    "DPR": {
        "description": "DPR (Dense Passage Retrieval) is a model that retrieves relevant passages from a large document collection to answer questions. It uses a bi-encoder architecture and has been trained on the Natural Questions dataset.",
        "website": "https://huggingface.co/transformers/model_doc/dpr.html",
    },
    "BART": {
        "description": "BART (Bidirectional and Auto-Regressive Transformers) is a sequence-to-sequence model that has achieved state-of-the-art performance on various NLP tasks such as text summarization and text generation.",
        "website": "https://huggingface.co/transformers/model_doc/bart.html",
    },
}

# Models
models = {
    "BERT": "bert-large-uncased-whole-word-masking-finetuned-squad",
    "DistilBERT": "distilbert-base-uncased-distilled-squad",
    "RoBERTa": "deepset/roberta-base-squad2",
    "ALBERT": "twmkn9/albert-base-v2-squad2",
    "Electra": "ahotrod/electra_large_discriminator_squad2_512",
    "XLNet": "xlnet-large-cased",
    "Longformer": "allenai/longformer-large-4096-finetuned-triviaqa",
    "SpanBERT": "mrm8488/spanbert-large-finetuned-squadv2",
    "T5": "valhalla/t5-base-qa-summary",
    "DPR": "facebook/dpr-question_encoder-single-nq-base",
    "BART": "facebook/bart-large-cnn",
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

def answer_question(inputs, question):
    input_ids = inputs["input_ids"].tolist()[0]
    answer_start_scores, answer_end_scores = model(**inputs).values()
    answer_start = torch.argmax(answer_start_scores).item()
    answer_end = torch.argmax(answer_end_scores).item() + 1
    answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end]))
    answer = answer.replace("[SEP]", "").strip()
    return answer

# Model selection
selected_model = st.sidebar.selectbox("Select Model", list(model_info.keys()))
default_temperature = 1.0
temperature = st.sidebar.slider(
    "Temperature | Creative >0.5", min_value=0.0, max_value=1.0, step=0.1, value=default_temperature
) 
if selected_model in ["T5", "BART"]:
    tokenizer = T5Tokenizer.from_pretrained(selected_model)
    model = T5ForConditionalGeneration.from_pretrained(selected_model)
else:
    tokenizer = AutoTokenizer.from_pretrained(models[selected_model])
    model = AutoModelForQuestionAnswering.from_pretrained(models[selected_model])
# Metrics
num_models = len(model_info)
num_models_new = 0
num_urls_entered = 0
num_urls_processed = 0
num_documents_entered = 0
num_documents_processed = 0

# Streamlit app
# st.title("Document Question Answering")
st.subheader("Upload a document or enter a URL to answer questions about the content.")

# Increment model count
num_models_new += 1

# Display metrics in a single row
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Active Model", selected_model)
with col2:
    st.metric("Number of Models", num_models, num_models_new)
with col3:
    st.metric("URLs Processed", num_urls_entered, num_urls_processed)
with col4:
    st.metric("Documents Processed", num_documents_entered, num_documents_processed)

# Display model information
st.markdown("----")
display_model_info(selected_model)
st.markdown("----")
# Model loading

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
        # st.write("Text content:")
        # st.write(text_content)
    elif uploaded_file is not None:
        text_content = uploaded_file.read().decode("utf-8")
        st.write("File uploaded successfully.")
        # st.write("Text content:")
        # st.write(text_content)
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
            answer = answer_question(inputs, question)
            answers.append(answer)

        # Combine answers from different chunks
        answer = " ".join(answers)
        answer = answer.replace("[SEP]", "").strip()

        st.write("Answer:")
        st.write(answer)

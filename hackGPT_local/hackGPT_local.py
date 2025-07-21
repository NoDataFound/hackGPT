import streamlit as st
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from transformers import AutoTokenizer, AutoModelForQuestionAnswering

def download_webpage(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc.split(".")[0]
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")
    text_content = soup.get_text(separator=" ")
    return text_content

st.set_page_config(page_title="Document Question Answering", page_icon=":blue_book:", layout="wide")

st.image("https://raw.githubusercontent.com/NoDataFound/hackGPT/main/res/hackGPT_logo.png", width=80)
st.sidebar.markdown("""
    <center>
        <img src='https://raw.githubusercontent.com/NoDataFound/hackGPT/main/res/hackgpt_fav.png' alt='hackGPTlogo' width='64'/> 
        hackGPT with Local LLMs
    </center>
""", unsafe_allow_html=True)
st.sidebar.markdown("----")

model_info = {
    "BERT": {
        "description": "BERT (Bidirectional Encoder Representations from Transformers), is a transformer-based model that has achieved state-of-the-art performance on various NL tasks.",
        "website": "https://huggingface.co/transformers/model_doc/bert.html",
    },
    # ... other models omitted for brevity
}

models = {
    "BERT": "bert-large-uncased-whole-word-masking-finetuned-squad",
    # ... other models omitted for brevity
}

selected_model = st.sidebar.selectbox("Select Model", list(model_info.keys()))

tokenizer = AutoTokenizer.from_pretrained(models[selected_model])
model = AutoModelForQuestionAnswering.from_pretrained(models[selected_model])

st.title("Document Question Answering")

display_model_info = st.cache(suppress_st_warning=True)(lambda model_name: f"""
    <style>
        .model-info {{
            margin: 1rem 0;
        }}
    </style>
    <div class="model-info">
        <h3>{model_name}</h3>
        <p><strong>Description:</strong> {model_info[model_name]['description']}</p>
        <p><strong>Website:</strong> <a href="{model_info[model_name]['website']}" target="_blank">{model_name}</a></p>
    </div>
""")
display_model_info(selected_model)

url = st.sidebar.text_input("Enter a URL")
uploaded_file = st.sidebar.file_uploader("Upload a document")
question = st.text_input("Enter your question", key="question")

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
        max_chunk_length = 512
        document_chunks = [text_content[i:i + max_chunk_length] for i in range(0, len(text_content), max_chunk_length)]
        answers = []
        for chunk in document_chunks:
            inputs = tokenizer.encode_plus(question, chunk, max_length=512, truncation=True, return_tensors="pt")
            answer = model(**inputs).last_hidden_state[:, 0, :]
            answer = answer.tolist()[0]
            answers.append(answer)

        answer = " ".join([str(i) for i in answers])

        st.write("Answer:")
        st.write(answer)

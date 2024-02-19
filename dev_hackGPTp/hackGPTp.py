import streamlit as st
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import GPT4All, LlamaCpp
import argparse
import time
import os
import subprocess
import pandas as pd

# Load environment variables from .env file
load_dotenv()

# Set default values from environment variables
os.environ["TOKENIZERS_PARALLELISM"] = "false"
model_n_ctx = int(os.environ.get('MODEL_N_CTX', 1000))
model_n_batch = int(os.environ.get('MODEL_N_BATCH', 8))
target_source_chunks = int(os.environ.get('TARGET_SOURCE_CHUNKS', 4))
model_type = os.environ.get('MODEL_TYPE', 'GPT4All')
model_path = os.environ.get('MODEL_PATH', 'LLM/ggml-gpt4all-j-v1.3-groovy.bin')
embeddings_model_name = os.environ.get('EMBEDDINGS_MODEL_NAME', 'all-MiniLM-L6-v2')
persist_directory = os.environ.get('PERSIST_DIRECTORY')

# Set up the sidebar
st.sidebar.image('https://raw.githubusercontent.com/NoDataFound/hackGPT/main/res/hackGPT_logo.png', width=300)
github_logo = "https://raw.githubusercontent.com/NoDataFound/hackGPT/main/res/github.png"
hackGPT_repo = "https://github.com/NoDataFound/hackGPT"
st.sidebar.markdown(f"[![GitHub]({github_logo})]({hackGPT_repo} 'hackGPT repo')")

# Initialize the chat history data as a Pandas DataFrame
CSS = """
img {
    box-shadow: 0px 10px 15px rgba(0, 0, 0, 0.2);
}
"""
st.markdown(f'<style>{CSS}</style>', unsafe_allow_html=True)

# Define the main function
def main():
    # Parse command-line arguments
    args = parse_arguments()

    # Initialize the language model
    callbacks = [] if args.mute_stream else [StreamingStdOutCallbackHandler()]
    if model_type == "LlamaCpp":
        llm = LlamaCpp(model_path=model_path, n_ctx=model_n_ctx, n_batch=model_n_batch, callbacks=callbacks, verbose=False)
    elif model_type == "GPT4All":
        llm = GPT4All(model=model_path, n_ctx=model_n_ctx, backend='gptj', n_batch=model_n_batch, callbacks=callbacks, verbose=False)
    else:
        raise Exception(f"Model type {model_type} is not supported. Please choose one of the following: LlamaCpp, GPT4All")

    # Initialize the RetrievalQA chain
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=not args.hide_source)

    # Get user input
    query = st.text_input("", value="Ask your question", key="question_input")
    submit_button = st.button("Submit")

    if submit_button:
        st.spinner("Processing Question")
        start = time.time()
        res = qa(query)
        answer, docs = res['result'], [] if args.hide_source else res['source_documents']
        end = time.time()

        st.code(f"> Answer (took {round(end - start, 2)} s.):")
        st.success(answer)

        for document in docs:
            st.code("Answer derived from " + document.metadata["source"] + " in this section: ")
            st.info(document.page_content)

# Parse command-line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description='privateGPT: Ask questions to your documents without an internet connection, using the power of LLMs.')
    parser.add_argument("--hide-source", "-S", action='store_true',
                        help='Use this flag to disable printing of source documents used for answers.')

    parser.add_argument("--mute-stream", "-M",
                        action='store_true',
                        help='Use this flag to disable the streaming StdOut callback for LLMs.')

    return parser.parse_args()

if __name__ == "__main__":
    main()

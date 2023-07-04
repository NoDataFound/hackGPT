import streamlit as st
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import GPT4All, LlamaCpp
import os

load_dotenv()

# Set default values from .env
model_n_ctx = int(os.environ.get('MODEL_N_CTX', 1000))
model_n_batch = int(os.environ.get('MODEL_N_BATCH', 8))
target_source_chunks = int(os.environ.get('TARGET_SOURCE_CHUNKS', 4))
model_type = os.environ.get('MODEL_TYPE', 'GPT4All')
model_path = os.environ.get('MODEL_PATH', 'LLM/ggml-gpt4all-j-v1.3-groovy.bin')
embeddings_model_name = os.environ.get('EMBEDDINGS_MODEL_NAME', 'all-MiniLM-L6-v2')

# Set up the sidebar
st.sidebar.title("Settings")
with st.sidebar.expander("Settings"):
    model_n_ctx = st.slider("MODEL_N_CTX", min_value=100, max_value=5000, value=model_n_ctx)
    model_n_batch = st.slider("MODEL_N_BATCH", min_value=1, max_value=16, value=model_n_batch)
    target_source_chunks = st.slider("TARGET_SOURCE_CHUNKS", min_value=1, max_value=10, value=target_source_chunks)
    model_type = st.selectbox("MODEL_TYPE", ['LlamaCpp', 'GPT4All'], index=0 if model_type == 'LlamaCpp' else 1)
    model_path = st.text_input("MODEL_PATH", value=model_path)
    embeddings_model_name = st.text_input("EMBEDDINGS_MODEL_NAME", value=embeddings_model_name)

from constants import CHROMA_SETTINGS

def main():
    # Load the embeddings model
    embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)

    # Set up the file upload
    st.sidebar.title("File Upload")

    # Create the "input/files" directory if it doesn't exist
    os.makedirs("input/files", exist_ok=True)

    # Read the uploaded files in the "input/files" directory
    uploaded_files = [os.path.join("input/files", filename) for filename in os.listdir("input/files")]

    # File uploader
    uploaded_file = st.sidebar.file_uploader("Choose a file", type=["pdf", "txt"])
    if uploaded_file is not None:
        # Save the uploaded file
        file_path = save_uploaded_file(uploaded_file)
        st.sidebar.success("File uploaded successfully.")
        uploaded_files.append(file_path)

    # Multi-select for selecting documents
    selected_documents = st.multiselect("Selected Documents", uploaded_files)

    # Process button
    if st.button("Process") and selected_documents:
        with st.spinner("Processing the document..."):
            try:
                document_text = process_documents(selected_documents)
                st.success("Document processed. Ready for questions.")
                display_document_info(selected_documents, document_text)
            except Exception as e:
                st.error(f"Error: {str(e)}")

    # Question form
    query = st.text_input("Ask your question", value="", key="question_input")
    submit_button = st.button("Submit")

    document_text = ""  # Initialize the variable here
    for document in selected_documents:
        read_doc = document
        with open(str(read_doc), "r") as f:
            document_text += f.read().strip() + " "

    if submit_button and query:
        st.title("Results")

        # Prepare the retrieval QA
        db = Chroma(persist_directory="db", embedding_function=embeddings, client_settings=CHROMA_SETTINGS)
        retriever = db.as_retriever(search_kwargs={"k": target_source_chunks})

        # Prepare the LLM
        if model_type == "LlamaCpp":
            llm = LlamaCpp(model_path=model_path, n_ctx=model_n_ctx, n_batch=model_n_batch, verbose=False)
        elif model_type == "GPT4All":
            llm = GPT4All(model=model_path, n_ctx=model_n_ctx, backend='gptj', n_batch=model_n_batch, verbose=False)
        else:
            raise Exception(f"Model type {model_type} is not supported. Please choose one of the following: LlamaCpp, GPT4All")

        qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True)

        # Get the answer from the chain
        try:
            st.info("Processing the question...")
            chunks = split_text_into_chunks(document_text, model_n_ctx)
            answer = ""
            docs = []
            for chunk in chunks:
                res = qa(chunk, query)
                answer += res['result'] + " "
                docs.extend(res['source_documents'])
            st.success("Question processed.")

            # Print the result
            st.subheader("Question:")
            st.write(query)
            st.subheader("Answer:")
            st.write(answer.strip())

            # Print the relevant sources used for the answer
            for document in docs:
                st.subheader(document.metadata["source"])
                st.code(document.page_content)
        except Exception as e:
            st.error(f"Error: {str(e)}")

def save_uploaded_file(uploaded_file):
    file_name = uploaded_file.name
    file_path = os.path.join("input/files", file_name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path

def process_documents(selected_documents):
    document_text = ""
    for document_file in selected_documents:
        with open(document_file, "r") as f:
            text_content = f.read().strip()
        document_text += text_content + " "
    return document_text.strip()

def display_document_info(selected_documents, document_text):
    # Document information
    st.subheader("Document Information")

    # Display file names
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("Filename:")
        for document_file in selected_documents:
            st.write(os.path.basename(document_file))

    # Display word count
    with col2:
        word_count = len(document_text.split())
        st.write("Word Count:")
        st.write(word_count)

    # Display total length
    with col3:
        total_length = len(document_text)
        st.write("Total Length:")
        st.write(total_length)

    # Display five lines of text
    #st.write("Text Sample:")
    lines = document_text.split("\n")[:5]
    st.code("\n".join(lines))

def split_text_into_chunks(text, chunk_size):
    chunks = []
    while len(text) > chunk_size:
        chunks.append(text[:chunk_size])
        text = text[chunk_size:]
    if text:
        chunks.append(text)
    return chunks

if __name__ == "__main__":
    main()

import os
from dotenv import load_dotenv  # Import the load_dotenv function from the dotenv module
from chromadb.config import Settings  # Import the Settings class from the chromadb.config module

# Load environment variables from a .env file
load_dotenv()

# Define the folder for storing the database
PERSIST_DIRECTORY = os.environ.get('PERSIST_DIRECTORY')

# Define the Chroma settings
CHROMA_SETTINGS = Settings(
    chroma_db_impl='duckdb+parquet',  # Choose the database implementation and format
    persist_directory=PERSIST_DIRECTORY,
)

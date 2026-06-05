\# PDF RAG Chatbot (From Scratch)



A Retrieval-Augmented Generation (RAG) chatbot built from scratch using Python, Sentence Transformers, cosine similarity retrieval, and Google's Gemini API.



The system allows users to upload PDF documents, generate embeddings, store document knowledge locally, and ask questions grounded in the uploaded document.



\## Features



\* PDF text extraction

\* Text cleaning and preprocessing

\* Overlapping text chunking

\* Semantic embeddings using Sentence Transformers

\* Vector storage using NumPy

\* Top-K retrieval using cosine similarity

\* Prompt engineering for grounded responses

\* Gemini API integration for answer generation

\* Multi-document support

\* Automated document ingestion pipeline



\## Project Architecture



\### Document Ingestion Pipeline



PDF Document

→ Text Extraction

→ Text Cleaning

→ Chunking

→ Embedding Generation

→ Save Chunks

→ Save Embeddings



Generated files are stored inside:



vector\_db/



document\_name/



\* chunks.json

\* embeddings.npy



\### Question Answering Pipeline



User Question

→ Query Embedding

→ Cosine Similarity Search

→ Top-K Retrieval

→ Prompt Construction

→ Gemini LLM

→ Final Answer



\## Technologies Used



\* Python

\* Sentence Transformers

\* NumPy

\* Scikit-learn

\* PyPDF

\* Google Gemini API

\* JSON



\## Project Structure



RAG\_Project/



models/



\* embedding\_model.py

\* gemini\_model.py



pdf\_reader.py

chunking.py

create\_embeddings.py



ingest.py



retrieve.py

prompt\_builder.py

generate\_answer.py



ask.py



\## Installation



Clone the repository:



git clone <repository-url>



Install dependencies:



pip install -r requirements.txt



Create a .env file:



GEMINI\_API\_KEY=YOUR\_API\_KEY



\## Usage



\### Step 1: Ingest a PDF



Run:



python ask.py



Provide the PDF path when prompted.



The system automatically:



\* Extracts text

\* Creates chunks

\* Generates embeddings

\* Stores the vector database



\### Step 2: Ask Questions



After ingestion, ask questions related to the uploaded document.



Example:



Question:

What is a research problem?



Answer:

A research problem is the first and most important step in the research process...



\## Sample Capabilities



\* Semantic document search

\* Academic PDF question answering

\* Knowledge-base chatbot

\* Research document exploration

\* Study material assistant



\## Future Improvements



\* FAISS vector database integration

\* Streamlit web interface

\* Source citation support

\* Hybrid search (keyword + semantic search)

\* Conversation memory

\* Multi-PDF retrieval



\## Learning Outcomes



This project was built without LangChain to gain a deeper understanding of:



\* Embeddings

\* Vector Search

\* Cosine Similarity

\* Retrieval-Augmented Generation (RAG)

\* Prompt Engineering

\* LLM Integration

\* End-to-End AI Application Development




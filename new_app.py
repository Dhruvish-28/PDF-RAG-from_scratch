import streamlit as st
import pandas as pd
import numpy as np
import faiss
import json
import os

from ingestion import ingest_multiple
from generate_answer import generate_answer

if "messages" not in st.session_state:
        st.session_state.messages = []

if "loaded" not in st.session_state:
        st.session_state.loaded = False

def process_files(files):

    pdf_paths = []

    os.makedirs("temp", exist_ok=True)

    for file in files:

        temp_path = f"temp/{file.name}"

        with open(temp_path, "wb") as f:
            f.write(file.getbuffer())

        pdf_paths.append(temp_path)

    metadata = ingest_multiple(pdf_paths)

    chunks = load_chunks()
    index = load_index()
    embeddings = load_embeddings()

    st.session_state.chunks = chunks
    st.session_state.index = index
    st.session_state.chunk_embedding = embeddings
    st.session_state.metadata = metadata
    st.session_state.loaded = True

    return metadata

def load_chunks():

    with open(
        "vector_db/chunks.json",
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)

def load_index():

    return faiss.read_index(
        "vector_db/index.faiss"
    )

def load_embeddings():
    return (
        np.load( f"vector_db/embeddings.npy") 
    )

def process_question(question):

    selected_chunks , answer= generate_answer(question , st.session_state.chunks , st.session_state.chunk_embedding , st.session_state.index)

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })

    return selected_chunks, answer

def display_chat():

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown( message["content"])

def display_chunks(selected_chunks):

    with st.sidebar:

        with st.expander("Retrieved Chunks"):

            for i, chunk in enumerate(selected_chunks,start=1):

                st.write(f"Document: {chunk['document']}")

                st.write(f"Chunk {i}")

                st.caption(f"Page {chunk['page']} | Similarity {chunk['score']*100:.1f}%")

                st.write(chunk["chunk"])

                st.divider()

        
if __name__ == "__main__":

    st.set_page_config(
    page_title="PDF RAG Chatbot",
    page_icon="📄",
    layout="wide"
    )
    
    st.header("**RAG IMPLEMENTED STUDY ASSISTANT**")
    st.divider()


    question = st.chat_input("Enter your Question:")
    
    with st.sidebar:

        st.header("Document Upload")
            
        files = st.file_uploader("Upload your PDF" , type=["pdf"] , accept_multiple_files=True)


    if files:
        
        with st.sidebar:
            
            left, right = st.columns(2)
            process = left.button("Process PDFs")
            reset = right.button("Reset session")
    
            if process:
                with st.spinner("Processing..."):
                    
                    metadata = process_files(files)
                    df = pd.DataFrame({"index" : [1], "Total files": metadata["Documents"], "Total Pages": metadata["pages"] , "Total chunks" : metadata["total chunks"]})
                    st.table(df , hide_index = True)
                    
                    st.session_state.loaded = True
            
            if reset:
        
                st.session_state.loaded = False
                st.session_state.messages = []
                files = []
                st.rerun()
        
        if question:

            selected_chunks , answer = process_question(question)
        
            display_chunks(selected_chunks)

        display_chat()

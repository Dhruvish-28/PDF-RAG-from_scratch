import streamlit as st
import pandas as pd
import numpy as np
import time
import json
import os

from ingestion import ingest
from generate_answer import generate_answer

st.set_page_config(
    page_title="PDF RAG Chatbot",
    page_icon="📄",
    layout="wide"
)

if "messages" not in st.session_state:
    st.session_state.messages = []

st.header("**RAG IMPLEMENTED STUDY ASSISTANT**")
st.divider()

# st.badge("Upload your pdf:")
left, right = st.columns([1, 2])

with st.sidebar:

    st.header("Document Upload")
    
    # with left:
        
    file = st.file_uploader("Upload your PDF" , type=["pdf"])
    
if "document_name" not in st.session_state:
    st.session_state.document_name = None
    
if file is not None:
    st.success(f"Success ! You uploaded ''{file.name}''")
    
    temp_path = f"temp/{file.name}"

    os.makedirs("temp", exist_ok=True)

    with open(temp_path, "wb") as f:
        f.write(file.getbuffer())
    
   
    metadata = ingest(temp_path)
    document_name = metadata["Pdf name"]

    with st.sidebar:
        df = pd.DataFrame({"index" : [1], "Pdf Name": metadata["Pdf name"], "Pages": metadata["pages"] , "Total chunks" : metadata["total chunks"]})
        st.table(df , hide_index = True)
    
    chunk_embedding = np.load( f"vector_db/{document_name}/embeddings.npy") 

    with open( f"vector_db/{document_name}/chunks.json","r",encoding="utf-8") as f: 
        chunks = json.load(f)

    st.session_state.document_name = document_name
    st.session_state.chunks = chunks
    st.session_state.chunk_embedding = chunk_embedding

for message in st.session_state.messages:
                
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
question = st.chat_input("Enter your Question:")
    
if question:
    if file is None:
        st.warning("Upload a file first")
    else:
        if st.session_state.document_name is None:
            st.error("Upload PDF First")
    
        else:
            
            with st.chat_message("user"):
                st.write(question)

            with st.spinner("Thinking..."):

                selected_chunks , answer= generate_answer(question , st.session_state.chunks , st.session_state.chunk_embedding)
                st.subheader("Answer")

                with st.chat_message("assistant"):
                    st.markdown(answer)

                st.session_state.messages.append({ "role": "user", "content": question })

                st.session_state.messages.append({"role": "assistant", "content": answer})
                        
                with st.sidebar:
                    
                    with st.expander("Retrieved Chunks"):
                        for i, chunk in enumerate(selected_chunks, start=1):

                            score_percent = chunk["score"] * 100
                            st.write(f"Chunk {i}")
                            st.caption(f"Page {chunk['page']} | Similarity {score_percent:.1f}%")
                            st.write(chunk['chunk'])
                
                            st.divider()

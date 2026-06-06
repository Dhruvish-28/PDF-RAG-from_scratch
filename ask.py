import os
import json 
import numpy as np
from ingestion import ingest

from generate_answer import generate_answer
print("\nRAG Chatbot Ready")

documents = os.listdir("data") # List all documents in current directory
print(f"Available document: {documents}")
    
document_name = input("Enter document name: ")
ingest(document_name)

chunk_embedding = np.load( f"vector_db/{document_name}/embeddings.npy") # loads all chunk embeddings processed from ingest(document_name)

with open( f"vector_db/{document_name}/chunks.json","r",encoding="utf-8") as f: # loads all chunks in text form
    chunks = json.load(f)
    
while True:

    query = input("\nAsk Question or 'exit': ")

    if query.lower() == "exit":
        break

    answer = generate_answer(query , chunks , chunk_embedding) # Obtains LLM response

    return answer
# from embedding_model import model
from create_embeddings import generate_embeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import json 

chunk_embedding = np.load("vector_db/embeddings.npy")
with open("vector_db/chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)

def retrieval(query , top_k = 3):

    
    query_embedding = generate_embeddings(query)

    similarities = cosine_similarity( [query_embedding], chunk_embedding)

    similarities.sort()


    indices = np.argsort(similarities[0])[-top_k:][::-1]

    retrieved_chunks = []

    for idx in indices:
        retrieved_chunks.append({
            "index": idx,
            "score": similarities[0][idx],
            "chunk": chunks[idx]
        })

    return retrieved_chunks
        
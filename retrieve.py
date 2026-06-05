# from embedding_model import model
from ingestion import generate_embeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def retrieval(query , chunks , chunk_embedding,top_k = 3):
    
    query_embedding = generate_embeddings(query)

    similarities = cosine_similarity( [query_embedding], chunk_embedding)
    
    indices = np.argsort(similarities[0])[-top_k:][::-1]

    retrieved_chunks = []
        
    for idx in indices:

        score = float(similarities[0][idx])
        score = round(float(similarities[0][idx]), 4)
        retrieved_chunks.append({
            "index": idx,
            "score": score,
            "chunk": chunks[idx]
        })

    return retrieved_chunks
        
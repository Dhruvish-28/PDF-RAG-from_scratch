# from embedding_model import model
from ingestion import generate_embeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def retrieval(query , chunks , chunk_embedding,top_k = 3):
    """
    parameters: 
    query : user passed query,
    chunks : all the chunks made from uploaded pdf,
    chunk_embedding : embeddings made from chunks,
    top_k : top k chunks which are most similar to query
    """
    
    query_embedding = generate_embeddings(query)

    similarities = cosine_similarity( [query_embedding], chunk_embedding) # calculates similarity between user query and each chunk
    
    indices = np.argsort(similarities[0])[-top_k:][::-1] # sorts for highest similarities and takes top K

    retrieved_chunks = []
        
    for idx in indices:

        # converts numpy objects into normal floating numbers and select upto 4 decimal values
        score = float(similarities[0][idx])
        score = round(float(similarities[0][idx]), 4)
        
        retrieved_chunks.append({
            "index": idx,
            "score": score,
            "chunk": chunks[idx]
        })

    return retrieved_chunks
        
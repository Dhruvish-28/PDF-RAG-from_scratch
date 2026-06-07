from ingestion import generate_embeddings
# from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import faiss

def retrieval(query , chunks , chunk_embedding,index):
    """
    parameters: 
    query : user passed query,
    chunks : all the chunks made from uploaded pdf,
    chunk_embedding : embeddings made from chunks,
    top_k : top k chunks which are most similar to query
    """
    top_k = 3
    
    query_embedding = generate_embeddings(query)
    query_embedding = np.array( [query_embedding], dtype="float32")
    faiss.normalize_L2(query_embedding)
    

    # Below index searches top k defined chunks from index and then returns the indices
    scores, indices = index.search( query_embedding, top_k )

    retrieved_chunks = []
        
    for idx, score in zip( indices[0], scores[0]):
        
        retrieved_chunks.append({
            "index": int(idx),
            "page": chunks[idx]["page"],
            "score": round(float(score), 4),
            "chunk": chunks[idx]["chunk"]
        })

    return retrieved_chunks
        
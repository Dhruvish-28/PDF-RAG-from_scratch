from ingestion import generate_embeddings
# from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import faiss

def retrieval(query , chunks , chunk_embedding,index,convo):
    """
    parameters: 
    query : user passed query,
    chunks : all the chunks made from uploaded pdf,
    chunk_embedding : embeddings made from chunks,
    top_k : top k chunks which are most similar to query
    index: embeddings index HSFW
    convo : last 3 user assisstant conversation
    """
    top_k = 3

    if len(convo) >= 2:

        retrieval_query = (convo[-2]["content"] + " " + query)

    else:
        retrieval_query = query

    
    query_embedding = generate_embeddings(retrieval_query)
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
            "chunk": chunks[idx]["chunk"] ,
            "document" : chunks[idx]["document"]
        })

    return retrieved_chunks
        
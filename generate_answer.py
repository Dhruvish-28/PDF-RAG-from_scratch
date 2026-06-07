from retrieve import retrieval
from prompt_builder import build_prompt
from gemini_model import model

def generate_answer(query, chunks , chunk_embedding):
    """
    parameters:
    query : user passed query
    chunks : chunks from pdf
    chunk_embeddings : embeddings of all chunks

    passes all 3 things to retrieve.py to get top 3 relevant chunks and scores.
    Then control goes to prompt_builder to obtain prompt to be given to LLM
    At last LLM generates response
    """
    
    selected_chunks = retrieval(query, chunks , chunk_embedding)

    prompt,score = build_prompt(selected_chunks, query)
    
    response = model.generate_content(prompt)
    
    return selected_chunks, response.text
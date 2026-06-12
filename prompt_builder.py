def build_prompt(chunks , query,convo):
    """
    parameters: relevant chunks & user query
    Takes relevant chunks and user query and buils a prompt to pass to LLM to generate answers. Returns the prompt and relevancy score
    convo : last 3 user assisstant conversation
    """
    context = ""
    score = []
    
    formatted_conversation = "\n".join(
    f"{msg['role']}: {msg['content']}"
    for msg in convo
    )
    
    for i, chunk in enumerate(chunks, start=1):
        context += f"Chunk {i}:\n"
        context += chunk["chunk"]
        context += "\n\n"
        score.append(chunk['score'])

    prompt = f"""
    
You are an educational assistant.

Answer the question in detail using only recent conversation provided and provided context.

If the user asks:
- "What is..." → give definition first.
- "Explain..." → provide detailed explanation.
- "List..." → provide a list.

Requirements for 'Explain' or 'Describe' type statements:
- Give complete explanations.
- Include all important points.
- Use bullet points where appropriate.
- Do not summarize unless asked.
- If multiple factors, types, advantages or steps are mentioned, include all of them.
- If the answer is unavailable in the context, say so.

Recent conversation:
{formatted_conversation}

Context:
{context}

Question:
{query}
"""

    return prompt , score
    
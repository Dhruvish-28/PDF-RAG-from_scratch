def chunking(text , chunk_size , overlap):

    words = text.split()
    
    start = 0
    end = chunk_size
    chunks = []
    
    while start < len(words):
    
        chunk = " ".join(words[start:end]) # Instead of each word individual we are making them into sentence again 
        chunks.append(chunk)
    
        start = end - overlap
        end += chunk_size - overlap 

    return chunks
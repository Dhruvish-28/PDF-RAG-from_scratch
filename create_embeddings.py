from embedding_model import model

def generate_embeddings(chunks):
    return model.encode(chunks)
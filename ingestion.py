from embedding_model import model
from pypdf import PdfReader
import numpy as np
import json
import re
import os

def read_pdf(pdf_path):
    "Reads the pdf , extracts text amd returns cleaned text"

    reader = PdfReader(pdf_path) 

    page_count = len(reader.pages)

    pages = []

    for page_num, page in enumerate(reader.pages):
        text = page.extract_text()

        
        text = text.replace("\n", " ") # replace new line characters with spaces
        text = re.sub(r"\s+", " ", text) # removes extra spaces caused due to \n removal
        
        pages.append({
        "page": page_num + 1,
        "text": text
    })


    return page_count , pages

def create_chunk(text, chunk_size=100, overlap=20):
    """parameters: text (actual cleaned text returned from read_pdf func() 

    chunk_size = 300 (default) size each chunk will be broken into
    overlap = 50 (default) overlapping between each chunks to not loose any information mid chunk
    """
    words = text.split()

    chunks = []

    start = 0

    while start < len(words):

        end = start + chunk_size

        chunk = " ".join(words[start:end])

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks

def pages_chunk(pages):
    
    all_chunks = []

    for page_data in pages:

        page_chunks = create_chunk(page_data["text"])

        for chunk in page_chunks:

            all_chunks.append({
                "page": page_data["page"],
                "chunk": chunk
            })

    return all_chunks

def generate_embeddings(chunks):
    "creates embedding of created chunks through transformer model"

    return model.encode(chunks)


def ingest(pdf_path):

    """ integrates all the following functions:
    read_pdf(doc_name),
    chunk_text(text , chunk_size , overlap)
    generate_embeddings(chunks)

    Also saves the chunks and their embeddings to a newly created folder in JSON and .npy formats respectively
    chunks.json and embeddings.npy
    """
    pdf_name = os.path.splitext(
        os.path.basename(pdf_path)
    )[0]

    output_folder = f"vector_db/{pdf_name}"

    os.makedirs(output_folder, exist_ok=True)

    page_count , pages = read_pdf(pdf_path)

    chunks = pages_chunk(pages)
    
    chunk_texts = [c["chunk"] for c in chunks]
    
    embeddings = generate_embeddings(chunk_texts)

    with open(
        f"{output_folder}/chunks.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(chunks, f)

    np.save(
        f"{output_folder}/embeddings.npy",
        embeddings
    )

    metadata = {
        "Pdf name" : pdf_name,
        "pages" : page_count,
        "total chunks" : len(chunks),
        "chunks" : chunks
    }

    return metadata
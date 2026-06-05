from embedding_model import model
from pypdf import PdfReader
import numpy as np
import json
import re
import os

def read_pdf(doc_name):
    "Reads the pdf , extracts text amd returns cleaned text"

    reader = PdfReader(f"data/{doc_name}") 

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text

    text = text.replace("\n", " ") # replace new line characters with spaces
    text = re.sub(r"\s+", " ", text) # removes extra spaces caused due to \n removal

    return text


def chunk_text(text, chunk_size=300, overlap=50):
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


def generate_embeddings(chunks):
    "creates embedding of created chunks through transformer model"

    return model.encode(chunks)


def ingest(doc_name):

    """ integrates all the following functions:
    read_pdf(doc_name),
    chunk_text(text , chunk_size , overlap)
    generate_embeddings(chunks)

    Also saves the chunks and their embeddings to a newly created folder in JSON and .npy formats respectively
    chunks.json and embeddings.npy
    """

    output_folder = f"vector_db/{doc_name}" 

    os.makedirs(output_folder, exist_ok=True) #makes vector_db folder

    text = read_pdf(doc_name)

    chunks = chunk_text(text)

    embeddings = generate_embeddings(chunks)

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

    print(f"Ingestion Complete : {doc_name}")

    print(f"Chunks : {len(chunks)}")

    print(f"Saved To : {output_folder}")

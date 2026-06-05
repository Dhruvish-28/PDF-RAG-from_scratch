from embedding_model import model
from pypdf import PdfReader
import numpy as np
import json
import re
import os

def read_pdf(doc_name):

    reader = PdfReader(f"data/{doc_name}")

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text

    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)

    return text


def chunk_text(text, chunk_size=300, overlap=50):

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

    return model.encode(chunks)


def ingest(doc_name):

    output_folder = f"vector_db/{doc_name}"

    os.makedirs(output_folder, exist_ok=True)

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

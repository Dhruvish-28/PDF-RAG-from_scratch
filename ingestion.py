from embedding_model import model
from pymudpdf import PdfReader
from docx import Document
import numpy as np
import faiss
import json
import fitz
import re
import os
    
def read_pdf(pdf_path):
    "Reads the pdf , extracts text and returns cleaned text"

    doc = fitz.open(pdf_path)

    pages = []

    for page_num, page in enumerate(doc):

        text = page.get_text()

        text = pre_process_text(text)

        pages.append({
            "page": page_num + 1,
            "text": text
        })

    page_count = len(doc)

    doc.close()

    return page_count, pages

def read_docx(file_path):
     "Reads the docx , extracts text and returns cleaned text"

    doc = Document(file_path)

    text = "\n".join(
        para.text for para in doc.paragraphs
    )

    text = pre_process_text(text)

    pages = [{
        "page": None,
        "text": text
    }]

    return 1, pages

def read_txt(file_path):
     "Reads the txt , extracts text and returns cleaned text"

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = pre_process_text(text)

    pages = [{
        "page": None,
        "text": text
    }]

    return 1, pages

def pre_process_text(text):

    clean_text = text.strip()

    clean_text = re.sub(r'\r\n?', '\n', text)

    clean_text = re.sub(r'\n{3,}', '\n\n', text)

    clean_text = re.sub(r'[ \t]+', ' ', text)

    return clean_text
    
def read_document(file_path):
    "Master function to call all file reader functions"

    extension = os.path.splitext(file_path)[1].lower()

    match extension:

        case ".pdf":
            return read_pdf(file_path)

        case ".docx":
            return read_docx(file_path)

        case ".txt":
            return read_txt(file_path)

        case ".md":
            return read_txt(file_path)

        case _:
            raise ValueError(
                f"Unsupported file type: {extension}"
            )
            
def create_chunk(text):
    """
    
    """
    chunk_size = 200
    overlap = 40
    
    paragraphs = re.split(r'\n\s*\n', text)

    chunks = []
    
    for paragraph in paragraphs:

        word_count = len(paragraph.split())

        if word_count <= chunk_size:

            chunks.append(paragraph)

        else:

            # old overlapping chunking logic
            
            start = 0
        
            while start < len(paragraph):
        
                end = start + chunk_size
        
                chunk = " ".join(words[start:end])
        
                chunks.append(chunk)
        
                start += chunk_size - overlap

    return chunks

def pages_chunk(pages , pdf_name):
    
    all_chunks = []

    for page_data in pages:

        page_chunks = create_chunk(page_data["text"])

        for chunk in page_chunks:

            all_chunks.append({
                "document" : pdf_name,
                "page": page_data["page"],
                "chunk": chunk
            })

    return all_chunks

def generate_embeddings(chunks):
    "creates embedding of created chunks through transformer model"

    return model.encode(chunks)


def ingest_multiple(pdf_path):

    """ integrates all the following functions:
    read_pdf(doc_name),
    chunk_text(text , chunk_size , overlap)
    generate_embeddings(chunks)

    Also saves the chunks and their embeddings to a newly created folder in JSON and .npy formats respectively
    chunks.json and embeddings.npy
    """
    all_chunks = []
    all_embeddings = []
    total_pages=0
    documents = 0


    for file in pdf_path:

        file_name = os.path.splitext(
            os.path.basename(file)
        )[0]

        documents += 1
        
        page_count , pages = read_document(file)

        total_pages += page_count

        chunks = pages_chunk(pages , file_name)

        all_chunks.extend(chunks)
        
        chunk_texts = [c["chunk"] for c in chunks]
    
        embeddings = generate_embeddings(chunk_texts)

        all_embeddings.append(embeddings)

    output_folder = f"vector_db"

    os.makedirs(output_folder, exist_ok=True)
    
    if len(all_embeddings) == 0:
        raise ValueError(
        f"No embeddings generated. pdf_path={pdf_path}"
    )

    all_embeddings = np.vstack(all_embeddings)
    
    all_embeddings = all_embeddings.astype("float32")

    dimension = embeddings.shape[1]

    faiss.normalize_L2(all_embeddings)
    
    index = faiss.IndexHNSWFlat(dimension, 32)

    index.add(all_embeddings)

    faiss.write_index(
    index,
    f"{output_folder}/index.faiss"
    )
    
    with open(
        f"{output_folder}/chunks.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(all_chunks, f)

    np.save(
        f"{output_folder}/embeddings.npy",
        all_embeddings
    )

    metadata = { 
        "Documents" : len(documents), 
        "pages" : total_pages , 
        "total chunks" : len(all_chunks)
    }

    return metadata
# Multi-PDF RAG Chatbot with FAISS and Gemini

A Retrieval-Augmented Generation (RAG) chatbot that allows users to upload and query multiple PDF documents simultaneously. The system uses Sentence Transformers for embeddings, FAISS for vector retrieval, and Gemini 2.5 Flash for answer generation.

The chatbot performs semantic search across all uploaded documents, retrieves the most relevant chunks, and generates context-aware answers with document and page references.

---

## Why Build Without LangChain?

This project intentionally avoids LangChain to gain hands-on understanding of:

- PDF Processing
- Chunking Strategies
- Embedding Generation
- Vector Storage
- Semantic Retrieval
- Prompt Construction
- LLM Integration

Every stage of the RAG pipeline is implemented manually.

## 📸 Application Preview

### Main Interface

![Application interface](results/WEB_UI.png)

### Retrieval Transparency

![Working model](results/working.png)

### Working Demo: Checkout releases

Shows:
- Application UI
- Working model

## 🔍 Retrieval Transparency

The system exposes retrieved chunks to the user.

For every answer the application displays:

- Document Name
- Similarity Score
- Source Page Number
- Retrieved Context

This allows users to verify where information originated before trusting the generated answer.

## 🚀 Features

- Multi-PDF document upload
- Unified knowledge base across uploaded PDFs
- Semantic chunking and embedding generation
- FAISS IndexFlatIP vector retrieval
- Cross-document retrieval
- Document and page-level source tracking
- Similarity score display
- Interactive chat interface using Streamlit
- Retrieved chunk transparency
- Reset knowledge base functionality
- Chat history support
---

# 🏗️ System Architecture

## Document Ingestion Pipeline

```text
PDF Upload
↓
PDF Extraction
↓
Chunking
↓
Embedding Generation
↓
FAISS Index Creation
      
```

Generated files are stored as:

```text
vector_db/

├── chunks.json
└── embeddings.npy
└── index.faiss

---

## Retrieval Pipeline

1. Upload one or more PDF documents.
2. Extract text page-by-page.
3. Generate overlapping chunks.
4. Convert chunks into dense vector embeddings.
5. Build a unified FAISS index.
6. Convert user query into embedding.
7. Retrieve Top-K relevant chunks.
8. Construct context-aware prompt.
9. Generate answer using Gemini.

---

## Example Retrieval Output

Document: MachineLearning.pdf
Page: 12
Similarity: 91.3%

Document: DeepLearning.pdf
Page: 7
Similarity: 88.4%

Document: NLP.pdf
Page: 3
Similarity: 85.9%

---

## Results

- Supports simultaneous querying across multiple PDF documents.
- Retrieves the Top-K most relevant chunks using FAISS.
- Displays source document names, page numbers, and similarity scores.
- Provides transparent retrieval for easier debugging and evaluation.

---

# 📂 Project Structure

```text
RAG_Project/

RAG-Project/
│
├── app.py
├── ingestion.py
├── retrieve.py
├── generate_answer.py
├── prompt_builder.py
├── requirements.txt
│
├── vector_db/
│ ├── chunks.json
│ ├── embeddings.npy
│ └── index.faiss
│
├── temp/
│
└── README.md
```

---
## Why FAISS?

The initial version of this project used brute-force cosine similarity retrieval.

This version integrates FAISS (Facebook AI Similarity Search) to provide an optimized vector search architecture while maintaining retrieval quality.

The project currently uses IndexFlatIP with L2-normalized embeddings to approximate cosine similarity search.

# 🧠 Retrieval Workflow

### Step 1: Document Embedding

Each PDF is:

1. Extracted
2. Cleaned
3. Split into overlapping chunks
4. Converted into embeddings
5. Stored locally

Example:

```text
Chunk 1 → [384 values]
Chunk 2 → [384 values]
Chunk 3 → [384 values]
...
```

---

### Step 2: Query Embedding

User Question:

```text
What should a research problem include
```

↓

```text
[384-dimensional query embedding]
```

---

### Step 3: Semantic Retrieval

The query embedding is compared with all document chunk embeddings using FAISS index

```text
Query
   │
   ▼
Cosine Similarity
   │
   ▼
Top-K Relevant Chunks
```

---

### Step 4: Answer Generation

Retrieved chunks are inserted into a prompt and passed to Gemini.

```text
Retrieved Context
       +
User Question
       │
       ▼
Gemini
       │
       ▼
Answer
```

---

# 🛠️ Technologies Used

| Category              | Technology            |
| --------------------- | --------------------- |
| Language              | Python                |
| Embeddings            | Sentence Transformers |
| Vector Storage        | NumPy                 |
| Retrieval             | Faiss index           |
| PDF Processing        | PyPDF                 |
| LLM                   | Google Gemini         |
| Environment Variables | python-dotenv         |
| Data Storage          | JSON                  |

| Parameter | Value |
|------------|--------|
| Embedding Model | all-MiniLM-L6-v2 |
| Embedding Dimension | 384 |
| Chunk Size | 100 words |
| Chunk Overlap | 20 words |
| Retrieval Engine | FAISS |
| Index Type | IndexFlatIP |
| Similarity | Cosine Similarity (Normalized Vectors) |
| LLM | Gemini 2.5 Flash |
# ⚙️ Installation

Clone the repository:

```bash
git clone <repository-url>
cd <repository-name>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env`file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

# ▶️ Usage

Initialise entry point by following command:
```bash
streamlit run app.py

Steps:

1. Upload a PDF
2. Wait for ingestion
3. Ask questions
4. View retrieved chunks and source pages
5. Inspect similarity scores


The system automatically:

* Extracts text
* Creates chunks
* Generates embeddings
* Stores the vector database

---

## Ask Questions

Example:

```text
Question:
What is a research problem?
```

```text
Answer:
A research problem is the first and most important step in the research process...
```

---

# 🎯 Sample Use Cases

* Academic PDF Question Answering
* Research Paper Exploration
* Study Material Assistant
* Internal Knowledge Base Search
* Semantic Document Search

---

## Future Improvements

- HNSW Approximate Nearest Neighbor Search
- Advanced Chunking Strategies
- Metadata-Based Filtering
- Conversation Memory
- Cloud Deployment
- Citation-Based Answer Generation

---


# 📚 Learning Outcomes

This project was built to understand the complete RAG pipeline without relying on abstraction frameworks.

Key concepts learned:

* Embeddings
* Vector Search
* Retrieval-Augmented Generation (RAG)
* Prompt Engineering
* Semantic Search
* LLM Integration
* End-to-End AI Application Development

---

## ⭐ Key Highlight

This project implements the core RAG workflow manually without LangChain, providing complete visibility into how document ingestion, embeddings, retrieval, prompt construction, and answer generation work under the hood.

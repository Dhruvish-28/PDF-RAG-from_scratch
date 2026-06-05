# 📄 PDF RAG Chatbot (From Scratch)

A Retrieval-Augmented Generation (RAG) chatbot built from scratch using Python, Sentence Transformers, Cosine Similarity Retrieval, and Google's Gemini API.

Unlike many RAG projects that rely on frameworks such as LangChain, this project implements the complete retrieval pipeline manually to gain a deeper understanding of embeddings, vector search, retrieval, prompt engineering, and LLM integration.

---

## 🚀 Features

* PDF Text Extraction
* Text Cleaning & Preprocessing
* Overlapping Text Chunking
* Semantic Embeddings using Sentence Transformers
* Vector Storage using NumPy
* Top-K Retrieval using Cosine Similarity
* Prompt Engineering for Grounded Responses
* Gemini API Integration
* Multi-Document Support
* Automated PDF Ingestion Pipeline
* Built Completely Without LangChain

---

# 🏗️ System Architecture

## Document Ingestion Pipeline

```text
PDF Document
      │
      ▼
Text Extraction
      │
      ▼
Text Cleaning
      │
      ▼
Chunking
      │
      ▼
Embedding Generation
      │
      ▼
Store Chunks + Embeddings
```

Generated files are stored as:

```text
vector_db/

├── document_1/
│   ├── chunks.json
│   └── embeddings.npy
│
├── document_2/
│   ├── chunks.json
│   └── embeddings.npy
```

---

## Question Answering Pipeline

```text
User Question
      │
      ▼
Query Embedding
      │
      ▼
Cosine Similarity Search
      │
      ▼
Top-K Retrieval
      │
      ▼
Prompt Construction
      │
      ▼
Gemini LLM
      │
      ▼
Final Answer
```

---

# 📂 Project Structure

```text
RAG_Project/

│
├── models/
│   ├── embedding_model.py
│   └── gemini_model.py
│
├── vector_db/
│
├── pdf_reader.py
├── chunking.py
├── create_embeddings.py
│
├── ingest.py
│
├── retrieve.py
├── prompt_builder.py
├── generate_answer.py
│
├── ask.py
│
├── requirements.txt
└── README.md
```

---

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
What is a research problem?
```

↓

```text
[384-dimensional query embedding]
```

---

### Step 3: Semantic Retrieval

The query embedding is compared with all document chunk embeddings using Cosine Similarity.

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
| Retrieval             | Cosine Similarity     |
| PDF Processing        | PyPDF                 |
| LLM                   | Google Gemini         |
| Environment Variables | python-dotenv         |
| Data Storage          | JSON                  |

---

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

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

# ▶️ Usage

## Ingest a PDF

Run:

```bash
python ask.py
```

Provide the PDF path when prompted.

Example:

```text
Enter PDF Path:
research_notes.pdf
```

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

# 🔮 Future Improvements

* FAISS Vector Database Integration
* Streamlit Web Interface
* Source Citation Support
* Hybrid Search (Keyword + Semantic)
* Conversation Memory
* Multi-PDF Retrieval
* Metadata-Based Filtering

---

# 📚 Learning Outcomes

This project was built to understand the complete RAG pipeline without relying on abstraction frameworks.

Key concepts learned:

* Embeddings
* Vector Search
* Cosine Similarity
* Retrieval-Augmented Generation (RAG)
* Prompt Engineering
* Semantic Search
* LLM Integration
* End-to-End AI Application Development

---

## ⭐ Key Highlight

This project implements the core RAG workflow manually without LangChain, providing complete visibility into how document ingestion, embeddings, retrieval, prompt construction, and answer generation work under the hood.

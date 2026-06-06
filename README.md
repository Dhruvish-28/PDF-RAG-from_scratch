# 📄 PDF RAG Chatbot (From Scratch)

## 📌 Project Overview

Built a Retrieval-Augmented Generation (RAG) chatbot from scratch without LangChain using Sentence Transformers, cosine similarity retrieval, Gemini 2.5 Flash, and Streamlit.

The system converts uploaded PDFs into vector embeddings, retrieves relevant document chunks using semantic search, and generates grounded answers while displaying source pages and retrieval scores for transparency.

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

Shows:
- Application UI
- Working model

## 🔍 Retrieval Transparency

The system exposes retrieved chunks to the user.

For every answer the application displays:

- Similarity Score
- Source Page Number
- Retrieved Context

This allows users to verify where information originated before trusting the generated answer.

## 🚀 Features

* PDF Text Extraction
* Text Cleaning & Preprocessing
* Overlapping Text Chunking
* Semantic Embeddings using Sentence Transformers
* Vector Storage using NumPy
* Top-K Retrieval using Cosine Similarity
* Prompt Engineering for Grounded Responses
* Gemini API Integration
* Automated PDF Ingestion Pipeline
* Built Completely Without LangChain

---

# 🏗️ System Architecture

## Document Ingestion Pipeline

```text
PDF Upload
      │
      ▼
Text Extraction
      │
      ▼
Page Metadata Capture
      │
      ▼
Chunking
      │
      ▼
Embedding Generation
      │
      ▼
Store:
  • Chunk Text
  • Page Number
  • Embeddings
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

│── embedding_model.py
│── gemini_model.py
│
├── vector_db/
│
├── pdf_reader.py
├── chunking.py
├── create_embeddings.py
│
├── ingestion.py
│
├── retrieve.py
├── prompt_builder.py
├── generate_answer.py
│
├── ask.py 
├── app.py
|
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
What should a research problem include
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

| Parameter | Value |
|------------|--------|
| Embedding Model | all-MiniLM-L6-v2 |
| Embedding Dimension | 384 |
| Chunk Size | 300 Words |
| Chunk Overlap | 50 Words |
| Top-K Retrieval | 3 |

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

## 7. Update Future Improvements

Current list includes Streamlit UI and Multi-PDF support, but you've already completed Streamlit. :contentReference[oaicite:3]{index=3}

Replace with:

```md
## 🔮 Future Improvements

- FAISS Integration
- Multi-PDF Retrieval
- Cross-Document Search
- Source Citations in Answers
- Conversation Memory
- Metadata Filtering
- Retrieval Evaluation Metrics
- Cloud Deployment

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

# LangChain PDF Question Answering (Local RAG with Ollama)

A simple **Retrieval Augmented Generation (RAG)** project that allows you to **ask questions about a PDF document** using **LangChain** and a **local LLM (Phi-3 via Ollama)**.

The application loads a PDF, splits it into chunks, stores embeddings in a vector database, and retrieves relevant information to answer user questions.

This project runs **completely locally** — no API keys required.

---

# Project Overview

This project demonstrates how to build a **local document question-answering system** using:

* LangChain
* Ollama
* Phi-3 model
* FAISS vector database
* PDF document processing

Users can interact with the system from the terminal and ask questions related to the PDF.

---

# Architecture

PDF Document
↓
Document Loader
↓
Text Splitter
↓
Embeddings Generation
↓
Vector Database (FAISS)
↓
Retriever
↓
Local LLM (Phi-3 via Ollama)
↓
Answer Generation

---

# Technologies Used

* Python
* LangChain
* Ollama
* Phi-3 model
* FAISS Vector Store
* PyPDF

---

# Project Structure

```
langchain-pdf-qa
│
├── app.py
├── genai_sample_document.pdf
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Installation

## 1. Clone the Repository

```
git clone https://github.com/your-username/langchain-pdf-qa.git
cd langchain-pdf-qa
```

---

## 2. Create a Virtual Environment

```
python -m venv venv
```

Activate it:

### Windows

```
venv\Scripts\activate
```

---

## 3. Install Dependencies

```
pip install -r requirements.txt
```

---

# Install Ollama

Download Ollama from:

https://ollama.com

After installation, pull the **Phi-3 model**:

```
ollama pull phi3
```

---

# Run Ollama

Start the Ollama server:

```
ollama serve
```

---

# Run the Application

Execute the Python script:

```
python app.py
```

---

# Example Usage

```
Chat with your PDF
Type 'exit' to stop

Ask a question:
What is Generative AI?

Answer:
Generative AI refers to artificial intelligence systems capable of generating text, images, and other content.
```

---

# Key Features

* Runs **fully locally**
* No API keys required
* Uses **LangChain RAG pipeline**
* Supports **PDF-based question answering**
* Lightweight setup suitable for laptops

---

# How It Works

1. Load the PDF document.
2. Split the document into smaller chunks.
3. Generate embeddings using Ollama.
4. Store embeddings in a FAISS vector database.
5. Retrieve relevant chunks when a user asks a question.
6. Send context + question to the LLM.
7. Generate the final answer.

---

# Future Improvements

* Add Streamlit UI
* Support multiple PDFs
* Store vectors in ChromaDB
* Add conversation memory
* Deploy as a web application

---

# License

This project is open-source and available under the MIT License.

---

# Author

Pooja Khatri

---

# Acknowledgements

* LangChain
* Ollama
* FAISS
* Phi-3

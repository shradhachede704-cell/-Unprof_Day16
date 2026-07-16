# -Unprof_Day16
Python Intermediate Day 16 Assignment
# Smart PDF Search

## Project Overview

Smart PDF Search is an AI-powered command-line application that performs semantic search on PDF documents. It extracts text from PDFs, converts the text into embeddings using Sentence Transformers, stores them in a FAISS vector database, and retrieves the most relevant text based on natural language queries.

## Features

- Read PDF files
- Extract and clean text
- Split text into chunks
- Generate embeddings
- Store embeddings in FAISS
- Semantic search using natural language
- Fast and accurate retrieval

## Technologies Used

- Python
- PyMuPDF
- Sentence Transformers
- FAISS
- NumPy

## Workflow

PDF → Text Extraction → Cleaning → Chunking → Embeddings → FAISS → User Query → Search Results

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python app.py
```

## Example

Enter PDF filename:

```
sample.pdf
```

Ask Question:

```
What is Artificial Intelligence?
```

Output:

```
Artificial Intelligence is the simulation of human intelligence by machines...
```

## Future Improvements

- Multiple PDF support
- GUI using Streamlit
- Chat with PDFs
- RAG using LangChain

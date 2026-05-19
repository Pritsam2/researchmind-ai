# ResearchMind AI

Advanced Multi-Query Retrieval-Augmented Generation (RAG) System for Research Paper Understanding

---

## Overview

ResearchMind AI is an advanced Multi-Query RAG system designed to improve semantic retrieval and grounded question answering over research papers.

Unlike traditional single-query RAG pipelines, ResearchMind AI generates multiple semantic reformulations of a user's query using GPT-4.1-mini, retrieves information through multiple semantic retrieval paths, aggregates the retrieved context, removes duplicate results, and generates grounded research-focused responses using GPT-4.1.

The project demonstrates modern AI retrieval engineering concepts including:

- Multi-Query Retrieval
- Semantic Search
- Vector Databases
- Embeddings
- Grounded Generation
- Modular AI Architecture
- Research Paper Question Answering

---

# Features

- Multi-Query Query Expansion using GPT-4.1-mini
- Semantic Retrieval using OpenAI Embeddings
- FAISS Vector Database Integration
- Grounded Research Answer Generation
- PDF Research Paper Ingestion
- Automatic Chunking Pipeline
- Deduplication of Retrieved Context
- Modular AI Engineering Architecture
- Gradio User Interface

---

# Architecture

```text
Research Papers (PDFs)
          ↓
Document Loading
          ↓
Text Chunking
          ↓
OpenAI Embeddings
          ↓
FAISS Vector Database
          ↓
User Question
          ↓
Multi-Query Generation
          ↓
Multiple Semantic Retrievals
          ↓
Retrieval Aggregation
          ↓
Deduplication
          ↓
Context Construction
          ↓
GPT-4.1 Grounded Answer Generation
          ↓
Final Research Answer

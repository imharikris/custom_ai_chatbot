# 📄 Custom AI Chatbot (Website + PDF)

## Overview

This project is a **Retrieval-Augmented Generation (RAG)** based AI chatbot that answers user questions **strictly from provided website content and PDF documents**.

The chatbot does **not hallucinate**.  
If an answer is not present in the indexed data, it responds with:

> “I don’t know based on the provided documents.”

The app also includes an optional **Generative Chat mode** for general AI conversations.

---

## Features

- Website scraping and text preprocessing
- Large PDF ingestion (scoped for demo)
- Chunking with overlap
- Vector search using FAISS
- Document-grounded answers (Custom Agent mode)
- General AI chat (Gemini) with safe fallback
- ChatGPT-like UI using Streamlit
- Easy to reuse for new clients by replacing data

---

## Tech Stack

- Python 3.10+
- Google Gemini API (AI Studio)
- FAISS (vector database)
- Streamlit (chat UI)
- BeautifulSoup (web scraping)
- pdfplumber (PDF extraction)

---

## Project Structure

custom_ai_chatbot/
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .env.example
├── data/
│ ├── raw/
│ └── processed/
├── ingest/
├── embeddings/
├── rag/
└── vectorstore/

## Setup Instructions

1. Create virtual environment
   python -m venv venv
   source venv/bin/activate # Windows: venv\Scripts\activate

2. Install dependencies
   pip install -r requirements.txt

3. Configure API key
   Create a .env file using the template:
   GOOGLE_API_KEY=your_api_key_here
   ⚠️ Do NOT commit .env to GitHub.

4. Run the chatbot
   streamlit run app.py

Chat Modes
🔹 Custom Agent (RAG)
Answers strictly from indexed documents

Deterministic and factual

Safe for internal/company use

🔹 Generative Chat
General AI conversation

Uses Gemini directly

Includes retry and fallback handling

Scope Limitations
Demo indexes a limited number of PDF pages

No authentication included

No production hosting included

API usage beyond demo must use client’s API key

Reusing for New Clients
To reuse this chatbot for a new client:

Replace files in data/raw/

Re-run ingestion and embedding scripts

Start the app again

No core code changes required.

Future Enhancements
Cloud deployment

Authentication & user roles

Multi-document uploads

Source citation per answer

Analytics & logging

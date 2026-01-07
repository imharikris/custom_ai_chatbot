import faiss
import google as genai
import numpy as np 
import json
from config import client,EMBEDDING_MODEL

def load_faiss_index():
    return faiss.read_index("vectorstore/vector_store.index")

def load_chunks():
    with open("data/processed/chunks.json", "r", encoding="utf-8") as f:
        return json.load(f)
    
def embed_query(query):
    result = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=query,
    )
    return np.array([result.embeddings[0].values]).astype("float32")

def retrieve_similar_chunks(query, top_k=5):
    index = load_faiss_index()
    chunks = load_chunks()

    query_vector = embed_query(query)
    distances, indices = index.search(query_vector, top_k)

    return [chunks[i]["text"] for i in indices[0]]
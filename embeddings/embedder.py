import json
import os
from config import  client, EMBEDDING_MODEL

def embed_text(texts):
    embeddings = []

    for text in texts:
        response = client.models.embed_content(
            model=EMBEDDING_MODEL,
            contents=text
        )
        embeddings.append(response.embeddings[0].values)

    return embeddings

if __name__ =="__main__":
    with open("data/processed/chunks.json", "r", encoding="utf-8") as f:
        chunks = json.load(f)
        texts = [chunk["text"] for chunk in chunks]
        embeddings = embed_text(texts)
        
    with open("data/processed/embeddings.json", "w", encoding="utf-8") as out_f:
            json.dump(embeddings, out_f, ensure_ascii=False, indent=4)

    print(f"Generated embeddings for {len(embeddings)} chunks and saved to data/processed/embeddings.json")

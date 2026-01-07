import json
import tiktoken

def chunk_text(text, max_tokens=500, overlap=50):
    encoder = tiktoken.get_encoding("cl100k_base")
    tokens= encoder.encode(text)
    chunks = []
    start = 0
    chunk_id = 0

    while start < len(tokens):
        end = start + max_tokens
        chunk_tokens = tokens[start:end]
        chunk_text = encoder.decode(chunk_tokens)
        chunks.append({
            "id": chunk_id,
            "text": chunk_text
        })
        chunk_id += 1
        start += max_tokens - overlap
    return chunks

if __name__ == "__main__":
    with open("data/processed/combined_text.txt", "r", encoding="utf-8") as f:
        text = f.read()
        chunks = chunk_text(text)

        with open("data/processed/chunks.json", "w", encoding="utf-8") as out_f:
            json.dump(chunks, out_f, ensure_ascii= False, indent=4)
        
        print(f"Text chunked into {len(chunks)} chunks and saved to data/processed/chunks.json")

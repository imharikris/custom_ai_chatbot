import faiss
import numpy as np
import json

if __name__ == "__main__":
    with open("data/processed/embeddings.json", "r", encoding="utf-8") as f:
        embeddings = json.load(f)

    vectors = np.array(embeddings).astype("float32")
    dimension = vectors.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(vectors)

    faiss.write_index(index, "vectorstore/vector_store.index")
    print(f"FAISS vector store created with {index.ntotal} vectors and saved to vectorstore/vector_store.index")
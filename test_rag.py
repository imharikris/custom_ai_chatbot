from rag.retriever import retrieve_similar_chunks
from rag.answer_generator import generate_answer

question = "How do I install FastAPI?"
context = retrieve_similar_chunks(question)
answer = generate_answer(context, question)

print("Question:", question)
print("\nAnswer:", answer)    
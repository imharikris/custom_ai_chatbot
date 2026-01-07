import google as genai
from config import GENERATIVE_MODEL, client
from rag.prompt_builder import SYSTEM_PROMPT

def generate_answer(context_chunks, question):
    context_text = "\n\n".join(context_chunks)
    prompt = f"{SYSTEM_PROMPT}\n\nContext:\n{context_text}\n\nQuestion: {question}"

    response = client.models.generate_content(model=GENERATIVE_MODEL, contents=prompt, config={
            "temperature": 0.0,
            "max_output_tokens": 512
        })
    return response.text.strip()



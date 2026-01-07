import streamlit as st
from rag.retriever import retrieve_similar_chunks
from rag.answer_generator import generate_answer

st.set_page_config(page_title="Custom AI Chatbot", layout="centered")

st.title("📄 Custom AI Chatbot")
st.caption("Answers strictly from the provided documents")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input (STAYS AT BOTTOM)
user_query = st.chat_input("Ask a question about the documents")

if user_query:
    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_query}
    )
    with st.chat_message("user"):
        st.markdown(user_query)

    # Generate answer
    with st.spinner("Searching documents..."):
        context = retrieve_similar_chunks(user_query)
        answer = generate_answer(context, user_query)

    # Show assistant message
    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
    with st.chat_message("assistant"):
        st.markdown(answer)
        st.caption("📌 Answered from indexed documents")

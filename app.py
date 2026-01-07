import streamlit as st
from rag.retriever import retrieve_similar_chunks
from rag.answer_generator import generate_answer
from config import client, GENERATIVE_MODEL

st.set_page_config(page_title="Custom AI Chatbot", layout="centered")

# -----------------------
# SESSION STATE
# -----------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_mode" not in st.session_state:
    st.session_state.chat_mode = "Custom Agent"

# -----------------------
# HEADER (MODERN)
# -----------------------
col1, col2 = st.columns([8, 1])

with col1:
    st.markdown("## 💬 Custom AI Chatbot")
    st.caption(
        "Document-grounded assistant with optional general AI chat"
    )

with col2:
    if st.button("🗑️", help="Clear chat"):
        st.session_state.messages = []
        st.rerun()

# -----------------------
# MODE TOGGLE (CLEAN)
# -----------------------
st.session_state.chat_mode = st.radio(
    "",
    ["Custom Agent", "Generative Chat"],
    horizontal=True,
    label_visibility="collapsed"
)

if st.session_state.chat_mode == "Custom Agent":
    st.caption("📄 Answers strictly from indexed documents")
else:
    st.caption("🤖 General AI conversation")

st.divider()

# -----------------------
# CHAT HISTORY
# -----------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -----------------------
# CHAT INPUT (BOTTOM)
# -----------------------
user_query = st.chat_input("Ask a question")

if user_query:
    # User message
    st.session_state.messages.append(
        {"role": "user", "content": user_query}
    )
    with st.chat_message("user"):
        st.markdown(user_query)

    # Assistant logic
    if st.session_state.chat_mode == "Custom Agent":
        with st.spinner("Searching documents…"):
            context = retrieve_similar_chunks(user_query)
            answer = generate_answer(context, user_query)
    else:
        with st.spinner("Thinking…"):
            response = client.models.generate_content(
                model=GENERATIVE_MODEL,
                contents=user_query,
                config={"temperature": 0.7}
            )
            answer = response.text.strip()

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
    with st.chat_message("assistant"):
        st.markdown(answer)
        st.caption(
            "📌 Document answer"
            if st.session_state.chat_mode == "Custom Agent"
            else "🤖 General AI response"
        )

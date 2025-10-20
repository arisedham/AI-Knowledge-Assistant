import streamlit as st
import requests
import os

# Backend URL (update if Dockerized)
BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")

st.set_page_config(page_title="AI Knowledge Assistant", page_icon="🤖", layout="centered")

st.title("🧠 AI Knowledge Assistant")
st.write("Upload a PDF and ask natural-language questions about its content.")

# --- Session state for chat history ---
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- File Upload Section ---
st.sidebar.header("📂 Upload Document")
uploaded_file = st.sidebar.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file is not None:
    with st.spinner("Uploading and processing PDF..."):
        files = {"file": (uploaded_file.name, uploaded_file, "application/pdf")}
        try:
            response = requests.post(f"{BACKEND_URL}/api/upload", files=files)
            if response.status_code == 200:
                st.sidebar.success("✅ File uploaded and processed successfully!")
            else:
                st.sidebar.error(f"❌ Upload failed: {response.text}")
        except Exception as e:
            st.sidebar.error(f"Error: {e}")

st.markdown("---")

# --- Chat Interface ---
st.subheader("💬 Chat with your Document")

query = st.chat_input("Ask a question about your uploaded document...")

if query:
    with st.spinner("Thinking..."):
        try:
            response = requests.post(
                f"{BACKEND_URL}/api/query",
                json={"question": query},  # JSON payload for FastAPI
                headers={"Content-Type": "application/json"},
            )

            if response.status_code == 200:
                answer = response.json().get("answer", "No answer found.")
                # Save conversation
                st.session_state.chat_history.append(("🧑 You", query))
                st.session_state.chat_history.append(("🤖 Assistant", answer))
            else:
                st.error(f"Query failed: {response.text}")
        except Exception as e:
            st.error(f"Error querying backend: {e}")

# --- Display chat history ---
if st.session_state.chat_history:
    for role, message in st.session_state.chat_history:
        st.markdown(f"**{role}:** {message}")

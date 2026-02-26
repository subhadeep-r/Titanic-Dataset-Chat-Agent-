import os
import streamlit as st
import requests
import base64

st.set_page_config(page_title="Titanic Chatbot", layout="centered")
st.title("Titanic Dataset Chatbot")
st.markdown("Ask questions in plain English about the Titanic dataset and get text answers plus visualizations.")

# use environment variable with localhost fallback for development
backend_url = os.getenv("BACKEND_URL", "http://localhost:8000")

# optional warning if still using localhost in a deployed environment
if backend_url == "http://localhost:8000":
    st.warning("Using default localhost backend URL; set BACKEND_URL in production environment.")

question = st.text_input("Your question", value="What percentage of passengers were male on the Titanic?")
if st.button("Ask"):
    if not backend_url:
        st.error("Please provide a backend URL")
    else:
        try:
            resp = requests.post(f"{backend_url.rstrip('/')}/ask", json={"question": question}, timeout=15)
            resp.raise_for_status()
            data = resp.json()
            st.subheader("Answer")
            st.write(data.get("answer", "No answer returned."))
            img_b64 = data.get("image")
            if img_b64:
                st.subheader("Visualization")
                img_bytes = base64.b64decode(img_b64)
                st.image(img_bytes)
        except Exception as e:
            st.error(f"Error asking backend: {e}")

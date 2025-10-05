# app.py
# Streamlit frontend that uses summarizer.py

import streamlit as st
from summarizer import load_model, summarize_text, save_summary

st.title("📝 Text Summarizer App")
st.write("Paste some text or upload a .txt file to summarize.")

# Input text
txt = st.text_area("Enter text here", height=300)

# Upload file
file = st.file_uploader("Or upload a .txt file", type=["txt"])
if file:
    txt = file.read().decode("utf-8")

# Settings
max_len = st.slider("Max summary length", 50, 300, 120)
min_len = st.slider("Min summary length", 10, 100, 30)

if st.button("Summarize"):
    if not txt.strip():
        st.warning("Please enter some text or upload a file.")
    else:
        model = load_model()  # load the model
        summary = summarize_text(txt, max_length=max_len, min_length=min_len, model=model)
        st.success("Summary:")
        st.write(summary)
        save_summary(summary)
        st.info("Saved summary to outputs/summary.txt")

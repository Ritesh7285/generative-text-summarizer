# summarizer.py
# Contains functions for summarization using Hugging Face

from transformers import pipeline

def load_model(model_name="sshleifer/distilbart-cnn-12-6"):
    """Load summarization pipeline"""
    return pipeline("summarization", model=model_name)

def summarize_text(text, max_length=120, min_length=30, model=None):
    """Summarize a text string"""
    if model is None:
        model = load_model()
    result = model(text, max_length=max_length, min_length=min_length, do_sample=False)
    return result[0]["summary_text"]

def save_summary(summary, filename="outputs/summary.txt"):
    """Save summary to file"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(summary)

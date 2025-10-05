# Text Summarizer using Generative AI

A simple Python project that generates concise summaries from long text using **Hugging Face Transformers**.  
This project includes a **Streamlit interface** for easy interaction and demonstrates a basic Generative AI workflow suitable for beginner AI/ML enthusiasts.

---

## Features
- **Abstractive text summarization** (Generative AI)  
- **Text input or `.txt` file upload**  
- **Adjustable summary length** using sliders  
- **Outputs saved** for reporting and verification  
- Lightweight and CPU-friendly using `t5-small` model  

---

## Project Structure
text-summarizer/
│
├── summarizer.py # Core logic: model loading & summarization functions
├── app.py # Streamlit frontend
├── outputs/
│ └── summary.txt # Generated summary
├── screenshots/
│ └── streamlit_ui.png # Screenshot of app running
├── requirements.txt # Python dependencies
└── README.md # Project documentation

## Installation

1. Clone the repository:
```bash
git clone <repo-url>
cd text-summarizer
Install dependencies:

bash
Copy code
pip install -r requirements.txt
How to Run
Run the Streamlit app:

bash
Copy code
streamlit run app.py
Enter text in the text area or upload a .txt file.

Adjust minimum and maximum summary length using the sliders.

Click Summarize to generate the summary.

The summary will be displayed on the app and saved automatically in:

bash
Copy code
outputs/summary.txt
Demo

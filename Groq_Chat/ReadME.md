# 💬 Chat with Open Source LLMs — Powered by Groq ⚡️

Welcome to **LLM Chat Interface**, a dynamic AI chatbot built with **Streamlit** and **Groq API**, allowing users to chat with top open-source LLMs like LLaMA, Mistral, Gemma, and more — with lightning-fast performance and responsive UI! ⚡

> 🛠️ Developed as a part of my internship training program, this project focuses on practical applications of LLMs, RAG systems, and document-based querying using LangChain.  

---

## 🌟 Features

- ✅ Real-time conversations with open-source LLMs  
- 📄 Upload and query PDFs & DOCX files  
- 🧠 RAG (Retrieval Augmented Generation) integration for file-based Q&A  
- ⚡ Ultra-fast inference with **Groq API**  
- 🎨 Sleek and minimal interface via **Streamlit**  
- 🔁 Choose between multiple LLMs on the fly  
- 💼 Built with internship-driven learning and production-ready goals

---

## 🧰 Tech Stack

| Tech | Description |
|------|-------------|
| 🐍 Python | Core language |
| 📺 Streamlit | Frontend interface |
| 🔗 Groq API | High-speed LLM backend |
| 📚 LangChain | Orchestration for RAG pipelines |
| 📄 PyMuPDF, python-docx | PDF & DOCX parsing |
| 🧠 Open Source LLMs | LLaMA, Mistral etc. |
| ☁️ Streamlit Cloud  | Hosting and deployment |

---

## 🚀 Live Demo

👉 Try the app here:  
🔗 **[Live Chat App](https://grochat-707.streamlit.app/)**

Enjoy real-time conversations and ask questions from uploaded files — it’s fast, simple, and intelligent! 🧠📁

---

## 💻 Local Setup Instructions

Want to run this project on your system? Follow these steps:

```bash
# 1. Clone the repository
git clone https://github.com/your-username/your-repo-name.git

# 2. Navigate into the folder
cd your-repo-name

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set your Groq API Key (get it from https://console.groq.com)
export GROQ_API_KEY=your_key_here

# 5. Launch the Streamlit app
streamlit run app.py

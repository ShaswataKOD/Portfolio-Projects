import os
import time
import streamlit as st
import fitz  # PyMuPDF for PDF
import docx  # For DOCX
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

# ---------- Load API Key ----------
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")
if not groq_api_key:
    st.error("🚨 GROQ_API_KEY not found!")
    st.stop()

# ---------- Page Config ----------
st.set_page_config(page_title="SmartChat – AI with PDF/DOCX Power (RAG Enabled)", layout="centered")

# ---------- Init LangChain Chat ----------
chat = ChatGroq(
    temperature=0.5,
    model="llama3-8b-8192",
    groq_api_key=groq_api_key
)

# ---------- Session State ----------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

# ---------- Text Extraction Functions ----------
def extract_text_from_pdf(uploaded_file, max_pages=20):
    text = ""
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        for page in doc[:max_pages]:
            text += page.get_text()
    return text

def extract_text_from_docx(uploaded_file):
    doc = docx.Document(uploaded_file)
    return "\n".join(p.text for p in doc.paragraphs)

# ---------- RAG Indexing ----------
def create_vectorstore(text, max_chunks=300):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_text(text)[:max_chunks]
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.from_texts(chunks, embeddings)

# ---------- Upload and Index ----------
st.markdown("""
<h1 style="text-align:center; font-size: 32px; margin-top: 1rem; margin-bottom: 2rem; color:#8f94fb;">
🤖 SmartChat – Ask Me Anything with AI!
</h1>
""", unsafe_allow_html=True)

with st.expander("📁 Upload a document (PDF or DOCX)"):
    uploaded_file = st.file_uploader("", type=["pdf", "docx"])
    if uploaded_file:
        if uploaded_file.size > 50_000_000:
            st.warning("⚠️ This is a large file. Uploading may take longer.")
        file_ext = uploaded_file.name.split(".")[-1].lower()
        try:
            with st.spinner("⏳ Processing and indexing document..."):
                start_time = time.time()
                if file_ext == "pdf":
                    full_text = extract_text_from_pdf(uploaded_file)
                elif file_ext == "docx":
                    full_text = extract_text_from_docx(uploaded_file)
                st.session_state.vectorstore = create_vectorstore(full_text)
                st.success("✅ Document uploaded and indexed!")
                st.caption(f"⏱️ Time taken: {time.time() - start_time:.2f} seconds")
        except Exception as e:
            st.error(f"❌ Failed to read document: {e}")

# ---------- Display Chat History ----------
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for msg in st.session_state.chat_history:
    role = "🧑" if isinstance(msg, HumanMessage) else "🤖"
    bubble = "bubble-user" if isinstance(msg, HumanMessage) else "bubble-ai"
    content = msg.content.replace("\n", "<br>")
    st.markdown(f"""
    <div class="message" style="justify-content: {'flex-end' if role == '🧑' else 'flex-start'};">
        <div class="avatar">{role}</div>
        <div class="{bubble}">{content}</div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------- User Input ----------
with st.form(key="chat-form", clear_on_submit=True):
    user_input = st.text_input("💬 Ask anything (about the doc or general)...")
    send = st.form_submit_button("Send")

    if send and user_input.strip():
        st.session_state.chat_history = [msg for msg in st.session_state.chat_history if not isinstance(msg, SystemMessage)]
        st.session_state.chat_history.append(HumanMessage(content=user_input))

        # RAG - retrieve relevant chunks if vectorstore exists
        if st.session_state.vectorstore:
            docs = st.session_state.vectorstore.similarity_search(user_input, k=4)
            context = "\n".join([doc.page_content for doc in docs])[:3000]
            st.session_state.chat_history.insert(0, SystemMessage(
                content=f"Use this document content as context when answering:\n{context}"
            ))

        try:
            response = chat.invoke(st.session_state.chat_history)
            st.session_state.chat_history.append(AIMessage(content=response.content))
        except Exception as e:
            st.error(f"⚠️ Error calling Groq: {e}")

# ---------- Footer ----------
st.markdown("---")

# ---------- Styling ----------
st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
    background: radial-gradient(circle at top left, #121212, #1e1e2f);
    color: #e1e1e6;
    margin: 0;
    padding: 0;
}
.chat-container {
    display: flex;
    flex-direction: column;
    gap: 12px;
    padding: 1rem 0;
}
.avatar {
    font-size: 26px;
    margin: 4px 12px 0 12px;
}
.bubble-user {
    background: linear-gradient(to right, #4e54c8, #8f94fb);
    color: #fff;
    padding: 12px 16px;
    border-radius: 16px 16px 4px 16px;
    box-shadow: 0 0 15px rgba(79, 92, 255, 0.4);
    font-size: 16px;
    max-width: 80%;
    animation: fadeInUp 0.3s ease-out;
}
.bubble-ai {
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(8px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    color: #ffffff;
    padding: 12px 16px;
    border-radius: 16px 16px 16px 4px;
    font-size: 16px;
    max-width: 80%;
    animation: fadeInUp 0.3s ease-out;
}
input[type="text"] {
    background-color: #22232e;
    border: 1px solid #3b3b4f;
    border-radius: 10px;
    padding: 12px;
    color: #fff;
    font-size: 16px;
    width: 100%;
}
.stButton>button {
    background: linear-gradient(to right, #3f51b5, #5c6bc0);
    color: white;
    border: none;
    padding: 10px 24px;
    border-radius: 8px;
    font-size: 16px;
    cursor: pointer;
    transition: 0.2s ease;
    margin-top: 0.5rem;
}
.stButton>button:hover {
    background: linear-gradient(to right, #5c6bc0, #3f51b5);
    transform: scale(1.03);
}
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}
</style>
""", unsafe_allow_html=True)

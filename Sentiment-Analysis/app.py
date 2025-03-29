import streamlit as st
import pickle
import nltk
import os
import re
import string
import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer

# Set up NLTK directory
nltk_data_dir = os.path.join(os.getcwd(), "nltk_data")
os.makedirs(nltk_data_dir, exist_ok=True)
nltk.data.path.append(nltk_data_dir)

# Download NLTK resources
try:
    nltk.download("punkt", download_dir=nltk_data_dir)
    nltk.download("stopwords", download_dir=nltk_data_dir)
except Exception as e:
    st.error(f"⚠️ Error downloading NLTK resources: {e}")
    st.stop()

# Load Model & Vectorizer
try:
    model = pickle.load(open("model/ln_model.pkl", "rb"))
    vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))
except FileNotFoundError:
    st.error("⚠️ Model or Vectorizer not found! Please check the 'model' directory.")
    st.stop()

# Initialize NLP components
stop_words = set(stopwords.words("english"))
porter = PorterStemmer()

def preprocess(text):
    """Clean and preprocess user input text."""
    text = text.lower()
    text = re.sub(r'http\S+|www\.\S+', '', text)  # Remove URLs
    text = re.sub(r'[@#]\w+', '', text)  # Remove mentions & hashtags
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    tokens = word_tokenize(text)
    tokens = [porter.stem(word) for word in tokens if word not in stop_words]
    return " ".join(tokens)

# Streamlit UI Configuration
st.set_page_config(page_title="Sentiment Analyzer", layout="wide")

# Custom Styling for a Premium Look
st.markdown("""
    <style>
    body {background-color: #f4f6f9;}
    .big-title {text-align: center; font-size: 45px; font-weight: bold; color: #4A90E2;}
    .sub-title {text-align: center; font-size: 22px; color: #6C757D; margin-bottom: 20px;}
    .stTextArea textarea {border-radius: 12px; border: 2px solid #4A90E2; font-size: 16px;}
    .sentiment-box {padding: 20px; border-radius: 12px; font-weight: bold; text-align: center; font-size: 22px; margin-top: 20px;}
    .positive {background: linear-gradient(135deg, #D4EDDA, #A3E4D7); color: #155724; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);}
    .negative {background: linear-gradient(135deg, #F8D7DA, #F5B7B1); color: #721C24; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);}
    </style>
""", unsafe_allow_html=True)

# App Title & Subtitle
st.markdown("<div class='big-title'>🔍 Sentiment Analysis App</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Analyze text sentiment effortlessly with a sleek UI</div>", unsafe_allow_html=True)

# User Input
user_input = st.text_area("Type your text below:", "", height=150)

# Prediction Logic
if user_input.strip():
    processed_text = preprocess(user_input)
    vectorized_text = vectorizer.transform([processed_text])
    prediction = model.predict(vectorized_text)[0]
    sentiment = "Positive" if prediction >= 0.5 else "Negative"
    confidence = max(model.predict_proba(vectorized_text)[0])
    
    sentiment_class = "positive" if sentiment == "Positive" else "negative"
    st.markdown(f"<div class='sentiment-box {sentiment_class}'>\n"
                f"{sentiment} Sentiment ({confidence:.2f} Confidence)\n" 
                "</div>", unsafe_allow_html=True)

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center; font-size: 14px;'>Made with ❤️ using Streamlit</div>", unsafe_allow_html=True)


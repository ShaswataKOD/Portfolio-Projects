import streamlit as st
import pickle
import re
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
import time

#newly developed model 



# Download NLTK stopwords and punkt for tokenization
nltk.download('stopwords')
nltk.download('punkt')

# Initialize PorterStemmer and stopwords
porter = PorterStemmer()
stop_words = set(stopwords.words('english'))

# Load the pre-trained Logistic Regression model
with open('ln_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Load the TfidfVectorizer
with open('vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

# Function to preprocess and vectorize text input
def preprocess_and_vectorize(text):
    # Lowercase the text
    text = text.lower()
    
    # Remove links, special characters (@, #), and punctuation
    text = re.sub(r'http\S+|www.\S+', '', text)  
    text = re.sub(r'@\w+', '', text)             # Remove @ symbol
    text = re.sub(r'#\w+', '', text)             # Remove # symbol
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Remove stopwords
    tokens = [word for word in tokens if word not in stop_words]
    
    # Stemming
    tokens = [porter.stem(word) for word in tokens]
    
    # Join the tokens back into a single string
    cleaned_text = ' '.join(tokens)
    
    # Transform the text into a numerical vector
    vectorized_text = vectorizer.transform([cleaned_text])
    
    return vectorized_text

# Streamlit app title
st.set_page_config(page_title="Sentiment Analysis App", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
    body {
        background-color: #f9f9f9;  /* Light background color */
    }
    .title {
        text-align: center;
        font-size: 3rem;
        color: #FF6347;  /* Tomato color */
        font-family: 'Comic Sans MS', cursive, sans-serif;
        text-shadow: 2px 2px #ffcccb;  /* Soft shadow */
    }
    .subtitle {
        text-align: center;
        font-size: 1.5rem;
        color: #4682B4;  /* Steel Blue color */
        font-family: 'Arial', sans-serif;
        margin-bottom: 30px;
        font-style: italic;  /* Italic style */
    }
    .text-area {
        border-radius: 10px;
        border: 2px solid #FF6347;  /* Tomato color */
        padding: 10px;
        font-size: 1.2rem;
        font-family: 'Courier New', Courier, monospace;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        margin: auto;
    }
    .btn {
        background-color: #FF6347;  /* Tomato color */
        color: white;
        font-size: 1.5rem;
        border: none;
        border-radius: 5px;
        padding: 12px 24px;
        cursor: pointer;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: background-color 0.3s ease;
        display: block;
        margin: 0 auto;  /* Center the button */
    }
    .btn:hover {
        background-color: #ff4500;  /* Darker tomato color on hover */
    }
    .footer {
        text-align: center;
        font-size: 1rem;
        color: #555;
        margin-top: 40px;
        font-family: 'Arial', sans-serif;
    }
</style>
""", unsafe_allow_html=True)

# Add a header and subtitle
st.markdown('<h1 class="title">✨ Sentiment Analysis App ✨</h1>', unsafe_allow_html=True)
st.markdown('<h3 class="subtitle">Analyze the sentiment of your text and see if it\'s positive or negative!</h3>', unsafe_allow_html=True)

# Text input from the user
user_input = st.text_area("📝 Enter your text:", "", height=150)

# Style the text area using CSS
st.markdown("""
<style>
    div[data-baseweb="textarea"] {
        border-radius: 10px;
        border: 2px solid #FF6347;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# Button to make predictions
if st.button("🔍 Predict Sentiment", key="predict_btn", help="Click to analyze the sentiment!"):
    # Show a spinner while processing
    with st.spinner("🔄 Analyzing..."):
        time.sleep(1)  # Simulate a slight delay
        # Check if user input is not empty
        if user_input.strip():
            # Preprocess and vectorize the user input
            processed_input = preprocess_and_vectorize(user_input)
            
            # Use the model to make predictions (Logistic Regression outputs 0 or 1)
            prediction = model.predict(processed_input)
            score = model.predict_proba(processed_input)  # Get prediction probabilities
            
            # Display the prediction result with score
            if prediction[0] >= 0.5:
                st.success(f"🌟 The sentiment is **positive** with a score of **{score[0][1]:.2f}**.")
            else:
                st.error(f"💔 The sentiment is **negative** with a score of **{score[0][0]:.2f}**.")
        else:
            st.warning("⚠️ Please enter some text for analysis.")

# Add a footer
st.markdown("<div class='footer'>Made with ❤️ using Streamlit</div>", unsafe_allow_html=True)

import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Download only stopwords (no punkt needed now)
nltk.download('stopwords')

ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

# -----------------------------
# Text Preprocessing Function
# -----------------------------
def transform_text(text):
    text = text.lower()
    text = text.split()   # ✅ simple split instead of nltk tokenizer

    filtered_words = []

    for word in text:
        word = word.strip(string.punctuation)
        if word.isalnum() and word not in stop_words:
            filtered_words.append(ps.stem(word))

    return " ".join(filtered_words)

# -----------------------------
# Load Model & Vectorizer
# -----------------------------
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("📩 Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button("Predict"):

    if input_sms.strip() == "":
        st.warning("Please enter a message first.")
    else:
        # Preprocess
        transformed_sms = transform_text(input_sms)

        # Vectorize
        vector_input = tfidf.transform([transformed_sms])

        # Predict
        result = model.predict(vector_input)[0]

        # Display Result
        if result == 1:
            st.error("🚨 Spam Message")
        else:
            st.success("✅ Not Spam Message")

# 📧 Email / SMS Spam Classifier

## 🚀 Project Overview

- This project is a Machine Learning based web application that classifies Email or SMS messages as **Spam** or **Not Spam**.
- It uses Natural Language Processing (NLP) techniques to preprocess the text and a Multinomial Naive Bayes model to detect spam messages.
- The application is deployed using Streamlit, making it easy for anyone to use without coding.

## 📝 Problem Statement

- Spam messages are unwanted and can cause security risks. This project aims to automatically classify messages as Spam or Not Spam, helping users filter unwanted messages and improve communication efficiency.

## 🛠 Technologies Used

- Python – Programming language
- Pandas – Data manipulation
- NumPy – Numerical operations
- NLTK – Natural Language Processing (tokenization, stopword removal, stemming)
- Scikit-learn – Machine Learning library
- TF-IDF Vectorizer – Feature extraction from text
- Multinomial Naive Bayes – Machine Learning model for classification
- Streamlit – Web app deployment

## 📊 Model Details

**Text Preprocessing**:
  - Convert text to lowercase
  - Tokenization (splitting text into words)
  - Stopword removal (removing common words like “is”, “the”)
  - Stemming (reducing words to their root form)



**Feature Extraction**:
- Using TF-IDF Vectorizer to convert text into numerical features


**Model Training**:
- Tested multiple models

**Best Model**: 
- Multinomial Naive Bayes

**Evaluation Metrics**:
- Accuracy: Measures overall correctness
- Precision: Measures how many predicted spam messages are actually spam

## ⚡ How to Run the Code

- 1. Clone the repository or download the ZIP file

- 2. Install required packages:
     - pip install pandas numpy nltk scikit-learn streamlit
- 3. Run the Streamlit app:
     - streamlit run app.py
- 4. Open the web app in your browser
- 5. Enter any Email or SMS text and click Predict to see if it’s Spam or Not Spam

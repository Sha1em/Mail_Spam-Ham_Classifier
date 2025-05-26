import streamlit as st
import pickle
import os

# Load model and vectorizer
with open('spam_classifier.pkl', 'rb') as f:
    model = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# 🎨 Apply custom CSS
st.markdown("""
    <style>
        .main {
            background-color: #f4f4f8;
            padding: 20px;
        }
        .stTextArea textarea {
            font-size: 16px;
        }
        .header {
            font-size: 36px;
            font-weight: bold;
            color: #4B8BBE;
            margin-bottom: 20px;
        }
        .subheader {
            font-size: 18px;
            color: #333;
        }
        .footer {
            margin-top: 50px;
            font-size: 14px;
            color: #aaa;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# 🧠 Display title and instructions
st.markdown('<div class="header">📧 Email Spam Classifier</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Paste an email message below to check if it\'s spam or ham.</div>', unsafe_allow_html=True)

# 📥 Email input
email_text = st.text_area("✉️ Your Email Text", placeholder="Type or paste your email content here...")

# 📊 Accuracy (You can update this after model training)
st.markdown("**Model Accuracy:** 🎯 98.84% (Logistic Regression)")

# 🔍 Predict
if st.button("🔎 Classify"):
    if email_text.strip() == "":
        st.warning("⚠️ Please enter some email content to classify.")
    else:
        vect_text = vectorizer.transform([email_text])
        prediction = model.predict(vect_text)[0]
        result = "🚫 **Spam**" if prediction == 1 else "✅ **Ham**"
        st.success(f"Prediction: {result}")

# 📌 Footer
st.markdown("""
    <div class="footer">
        Made with ❤️ using Streamlit<br>
        <a href="https://github.com/Sha1em/Mail_Spam-Ham_Classifier" target="_blank">GitHub Repo</a>
    </div>
""", unsafe_allow_html=True)

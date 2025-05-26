import streamlit as st
import pickle

# Load model and vectorizer
with open('spam_classifier.pkl', 'rb') as f:
    model = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

st.title("📧 Email Spam Classifier")
st.write("Paste the content of your email below:")

# Text input
email_text = st.text_area("Email Text")

# Predict button
if st.button("Check if Spam"):
    if email_text.strip() == "":
        st.warning("Please enter some text.")
    else:
        # Vectorize and predict
        vect_text = vectorizer.transform([email_text])
        prediction = model.predict(vect_text)[0]
        result = "🚫 Spam" if prediction == 1 else "✅ Ham"
        st.success(f"Result: **{result}**")

# Divider
st.markdown("---")

# Sample Email Input Demo
st.subheader("📬 Sample Email Inputs")

st.markdown("**Example 1:**")
st.code("""Subject: You won a FREE vacation!
Click the link now to claim your reward 🎁""", language="text")
st.markdown("Model prediction: 🚫 **Spam**")

st.markdown("**Example 2:**")
st.code("""Subject: Meeting update
Let's reschedule the meeting to Thursday at 3 PM.""", language="text")
st.markdown("Model prediction: ✅ **Ham**")


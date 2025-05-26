📧 Email Spam-Ham Classifier with Streamlit Deployment
A machine learning project to classify emails as Spam or Ham (Not Spam) based on their textual content, using Logistic Regression, TF-IDF, and deployed using Streamlit.

📂 Project Structure
Mail_Spam-Ham_Classifier/
│
├── app.py                  # Streamlit frontend
├── spam_classifier.pkl     # Trained ML model
├── vectorizer.pkl          # TF-IDF vectorizer
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .gitignore              # Git ignore rules

🧠 How It Works
Preprocessed text data using TF-IDF vectorization
Trained a Logistic Regression classifier
Saved the model and vectorizer as .pkl files
Built an interactive frontend using Streamlit
User pastes email text → model predicts spam or ham ✅


🚀 Live Demo
👉 Click here to try the app: https://mailspam-hamclassifier-8plvextxopxmpfbxep6zxj.streamlit.app/
Paste your email content and classify in one click!


🛠️ Tech Stack
Python 🐍
Scikit-learn
Pandas
TF-IDF Vectorization
Logistic Regression
Streamlit

📚 Model Training Notebook
Model was trained using this Jupyter notebook:

[Trainer-Code]-Spam_Ham--Mail_Classifier.ipynb 
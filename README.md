# 🛡️ JobGuard - Fake Job Posting Detection

[![Live Demo](https://img.shields.io/badge/Live-Demo-success?style=for-the-badge&logo=streamlit)](https://jobguardd.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red?style=for-the-badge)

> 🚀 **Try the application here:** https://jobguardd.streamlit.app/

---

An AI-powered Fake Job Posting Detection System built using Natural Language Processing (NLP) and Machine Learning.

---

## 📌 Overview

JobGuard helps identify whether a job posting is **Real** or **Fake** by analyzing the job description using **TF-IDF Vectorization** and **Logistic Regression**.

This project demonstrates an end-to-end Machine Learning pipeline including:

- Data Cleaning
- Feature Engineering
- NLP
- Model Training
- Model Evaluation
- Model Deployment using Streamlit

---
## 📷 Preview

![JobGuard Screenshot](screenshots/home.png)

## 🚀 Features

- Detects Fake Job Postings
- TF-IDF Text Vectorization
- Logistic Regression Classifier
- Confidence Score
- Fake Job Probability
- Risk Level Indicator
- Interactive Streamlit Web Application

---

## 📊 Model Performance

| Metric | Value |
|---------|------:|
| Accuracy | **97.71%** |
| Fake Job Recall | **87%** |
| Fake Job Precision | **73%** |
| F1 Score | **80%** |

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- TF-IDF
- Logistic Regression
- Streamlit

---

## 📂 Project Structure

```text
JobGuard/
│
├── app.py
├── predict.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── README.md
└── Fake_Job_Posting_Detection.ipynb
```

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/JobGuard.git
```

Go inside the project

```bash
cd JobGuard
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python -m streamlit run app.py
```

---

## 📸 Screenshots

### Home Page

(Add screenshot here)

### Prediction Result

(Add screenshot here)

---

## 📊 Dataset

Fake Job Posting Dataset (Kaggle)

---

## 👨‍💻 Developer

**Gaurav Yadav**

---

## ⭐ Future Improvements

- Deep Learning (LSTM/BERT)
- Resume Analysis
- Company Verification
- Explainable AI (SHAP/LIME)
- Cloud Deployment
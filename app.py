import streamlit as st
from predict import predict_job

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="🛡️ JobGuard",
    page_icon="🛡️",
    layout="centered"
)

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("🛡️ JobGuard")

st.sidebar.markdown("""
## About

JobGuard is an AI-powered Fake Job Detection System.

### Technologies

- Python
- Scikit-Learn
- TF-IDF
- Logistic Regression
- Streamlit

### Model Performance

- Accuracy: **97.71%**
- Fake Job Recall: **87%**

### Developer

**Gaurav Yadav**
""")

# ---------------- MAIN TITLE ---------------- #

st.title("🛡️ JobGuard")

st.markdown("## Fake Job Posting Detection System")

st.write(
    "Paste a complete job description below and let AI determine "
    "whether it is a **Real Job** or **Fake Job**."
)

# ---------------- SAMPLE BUTTON ---------------- #

if st.button("📄 Load Sample Job"):

    st.session_state["sample_job"] = """
Python Developer

We are looking for an experienced Python Developer.

Requirements:
- Python
- Django
- Flask
- SQL
- REST APIs
- AWS

Benefits:
- Health Insurance
- Paid Leave
- Remote Work

Employment Type:
Full-time
"""

# ---------------- TEXT AREA ---------------- #

job = st.text_area(
    "Job Description",
    value=st.session_state.get("sample_job", ""),
    height=300,
    placeholder="Paste complete job description here..."
)

# ---------------- PREDICT BUTTON ---------------- #

if st.button("🔍 Analyze Job", use_container_width=True):

    if job.strip() == "":

        st.warning("⚠ Please enter a job description.")

    else:

        label, confidence, fake_probability = predict_job(job)

        st.divider()

        st.subheader("Prediction Result")

        if label == "Real Job Posting":
            st.success("✅ REAL JOB POSTING")
        else:
            st.error("⚠ FAKE JOB POSTING")

        st.metric(
            "Prediction Confidence",
            f"{confidence:.2f}%"
        )

        st.progress(confidence / 100)

        st.metric(
            "Fake Job Probability",
            f"{fake_probability:.2f}%"
        )

        # Risk Level

        if fake_probability < 30:
            st.success("🟢 Risk Level : LOW")

        elif fake_probability < 70:
            st.warning("🟠 Risk Level : MEDIUM")

        else:
            st.error("🔴 Risk Level : HIGH")

        st.divider()

        st.subheader("Prediction Probabilities")

        real_probability = 100 - fake_probability

        st.write("Real Job")

        st.progress(real_probability / 100)

        st.write(f"{real_probability:.2f}%")

        st.write("Fake Job")

        st.progress(fake_probability / 100)

        st.write(f"{fake_probability:.2f}%")

# ---------------- ABOUT MODEL ---------------- #

with st.expander("ℹ About This Model"):

    st.write("""
This project was developed using:

- TF-IDF Vectorization
- Logistic Regression
- Scikit-Learn
- Streamlit

Dataset:
Kaggle Fake Job Posting Dataset

Purpose:
To identify fraudulent job postings using Natural Language Processing.
""")

# ---------------- FOOTER ---------------- #

st.divider()

st.markdown(
    """
<div style='text-align:center'>

Made with ❤️ using Python • Scikit-Learn • Streamlit

© 2026 Gaurav Yadav

</div>
""",
unsafe_allow_html=True
)
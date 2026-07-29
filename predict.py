import pickle

# Load trained model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))


def predict_job(text):
    """
    Predict whether a job posting is Real or Fake.

    Returns:
        label (str)
        confidence (float)
        fake_probability (float)
    """

    # Convert text into TF-IDF features
    text_vector = vectorizer.transform([text])

    # Prediction
    prediction = model.predict(text_vector)[0]

    # Prediction probabilities
    probabilities = model.predict_proba(text_vector)[0]

    confidence = max(probabilities) * 100
    fake_probability = probabilities[1] * 100

    if prediction == 0:
        label = "Real Job Posting"
    else:
        label = "Fake Job Posting"

    return label, confidence, fake_probability


# Run only when this file is executed directly
if __name__ == "__main__":

    sample = """
    Python Developer

    We are hiring a Python Developer with experience in Django,
    Flask, SQL, REST APIs and AWS.

    Benefits:
    - Health Insurance
    - Remote Work
    - Paid Leave
    """

    label, confidence, fake_probability = predict_job(sample)

    print("Prediction :", label)
    print(f"Confidence : {confidence:.2f}%")
    print(f"Fake Job Probability : {fake_probability:.2f}%")
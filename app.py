import streamlit as st
import pandas as pd
import numpy as np
import cv2
import tensorflow as tf
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns

def load_model():
    """Load your trained deep learning model for image prediction."""
    model = tf.keras.models.load_model("oral_cancer_model.h5")  # Replace with your model file
    return model

def predict_cancer(params):
    """Simple logic-based prediction based on family history."""
    return "Cancer Detected" if params["Family_History"] == 1 else "No Cancer Detected"

def predict_image(image):
    """Process image and use CNN model for prediction."""
    model = load_model()
    image = image.resize((224, 224))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    prediction = model.predict(image)
    return "Cancer Detected" if prediction[0][0] > 0.5 else "No Cancer Detected"

def predict_halitosis(params):
    """Example rule-based prediction for halitosis detection."""
    return "Halitosis Detected" if params["H2S_ppb"] > 100 else "No Halitosis Detected"

st.set_page_config(page_title="Oral Cancer Prediction", layout="wide")
st.image("mukta_logo.png", width=150)  # Mukta Logo
st.title("Oral Cancer Prediction System")

menu = ["Oral Cancer Awareness", "Oral Cancer Prediction", "Image-Based Prediction", "Halitosis Detection", "Final Analysis"]
choice = st.sidebar.selectbox("Select Interface", menu)

if choice == "Oral Cancer Awareness":
    st.header("Oral Cancer Awareness")
    st.write("Oral cancer is a major public health concern worldwide. Early detection is crucial!")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Oral_cancer_2.jpg/800px-Oral_cancer_2.jpg")
    st.subheader("Key Facts")
    st.write("- Risk factors: Tobacco, Alcohol, Poor Oral Hygiene, HPV infection.")
    st.write("- Symptoms: Mouth sores, difficulty in chewing, white or red patches.")
    st.write("- Prevention: Regular check-ups, quitting tobacco, maintaining oral hygiene.")

elif choice == "Oral Cancer Prediction":
    st.header("Oral Cancer Prediction Based on Parameters")
    params = {}
    params["Family_History"] = st.selectbox("Family History of Cancer", [0, 1])
    params["Age"] = st.number_input("Age", 10, 100)
    params["Tobacco_Use"] = st.selectbox("Tobacco Use", ["Yes", "No"])
    params["Alcohol_Use"] = st.selectbox("Alcohol Use", ["Yes", "No"])
    params["Smoking"] = st.selectbox("Smoking", ["Yes", "No"])
    if st.button("Predict Cancer"):
        prediction = predict_cancer(params)
        st.success(prediction)

elif choice == "Image-Based Prediction":
    st.header("Upload an Image for Oral Cancer Prediction")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)
        if st.button("Predict from Image"):
            prediction = predict_image(image)
            st.success(prediction)

elif choice == "Halitosis Detection":
    st.header("Halitosis Detection")
    params = {}
    params["H2S_ppb"] = st.number_input("H2S Level (ppb)", 0, 500)
    params["CH3SH_ppb"] = st.number_input("CH3SH Level (ppb)", 0, 500)
    params["VSC_ppb"] = st.number_input("VSC Level (ppb)", 0, 500)
    params["Tongue_Coating_Score"] = st.number_input("Tongue Coating Score", 0, 10)
    if st.button("Detect Halitosis"):
        prediction = predict_halitosis(params)
        st.success(prediction)

elif choice == "Final Analysis":
    st.header("Final Prediction and Recommendations")
    cancer_prediction = predict_cancer({"Family_History": 1})  # Replace with actual data
    halitosis_prediction = predict_halitosis({"H2S_ppb": 200})  # Replace with actual data
    st.write(f"### Cancer Prediction: {cancer_prediction}")
    st.write(f"### Halitosis Detection: {halitosis_prediction}")
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/6c/Oral_cancer_stages.jpg")
    st.subheader("Precautions and Next Steps")
    st.write("- Visit a doctor if symptoms persist.")
    st.write("- Maintain oral hygiene.")
    st.write("- Quit smoking and avoid tobacco.")
import streamlit as st
import pandas as pd
from PIL import Image

# Set the page config
st.set_page_config(page_title="MUKTA Oral Cancer Detection", layout="wide")

# Load Mukta Logo
mukta_logo = "mukta_logo.png"  # Make sure this file exists in the same directory
st.sidebar.image(mukta_logo, width=200)

# Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["About Oral Cancer", "Oral Cancer Prediction", "Image Upload", "Halitosis Detection", "Final Results"])

# 1st Interface: Oral Cancer Awareness
if page == "About Oral Cancer":
    st.title("Oral Cancer Awareness")
    
    # Add a relevant image
    st.image("https://www.cancer.gov/sites/g/files/xnrzdm211/files/styles/cgov_article/public/cgov_image/media_image/160960_main.png", caption="Oral Cancer Awareness", use_column_width=True)
    
    # Add Detailed Information
    st.write("""
    ### What is Oral Cancer?
    Oral cancer refers to cancer that develops in the tissues of the mouth or throat. It is part of a group of cancers called head and neck cancers.
    
    ### Risk Factors:
    - Tobacco Use (Smoking & Chewing)
    - Excessive Alcohol Consumption
    - Poor Oral Hygiene
    - HPV Infection
    - Betel Nut Chewing
    
    ### Symptoms:
    - Persistent sores or ulcers in the mouth
    - Pain or difficulty swallowing
    - White or red patches in the mouth
    - Swelling in the jaw
    
    Early detection and prevention are key to successful treatment.
    """)

# 2nd Interface: Oral Cancer Prediction Based on Parameters
elif page == "Oral Cancer Prediction":
    st.title("Oral Cancer Prediction")

    # User Input Fields
    country = st.selectbox("Country", ["India", "USA", "UK", "Other"])
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    age = st.number_input("Age", min_value=1, max_value=100)
    tobacco_use = st.selectbox("Tobacco Use", [0, 1])
    alcohol_use = st.selectbox("Alcohol Use", [0, 1])
    socioeconomic_status = st.selectbox("Socioeconomic Status", ["Low", "Medium", "High"])
    diagnosis_stage = st.selectbox("Diagnosis Stage", ["Early", "Mid", "Late"])
    treatment_type = st.selectbox("Treatment Type", ["Surgery", "Radiation", "Chemotherapy", "Combination"])
    survival_rate = st.slider("Survival Rate (%)", min_value=0, max_value=100)
    hpv_related = st.selectbox("HPV Related", [0, 1])
    smoking = st.selectbox("Smoking", [0, 1])
    poor_oral_hygiene = st.selectbox("Poor Oral Hygiene", [0, 1])
    betel_nut_use = st.selectbox("Betel Nut Use", [0, 1])
    oral_symptoms = st.text_area("Describe Any Symptoms")
    family_history = st.selectbox("Family History of Cancer", [0, 1])

    if st.button("Predict"):
        if family_history == 1:
            st.error("Warning: High risk of Oral Cancer! Consult a doctor immediately.")
        else:
            st.success("No immediate risk detected. Maintain good oral hygiene.")

# 3rd Interface: Image Upload
elif page == "Image Upload":
    st.title("Upload Oral Cavity Image for Analysis")

    uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        st.success("Image uploaded successfully. (Note: No AI analysis yet)")

# 4th Interface: Halitosis Detection
elif page == "Halitosis Detection":
    st.title("Halitosis (Bad Breath) Detection")

    age = st.number_input("Age", min_value=1, max_value=100)
    sex = st.selectbox("Sex", ["Male", "Female", "Other"])
    groups = st.selectbox("Groups", ["Group 1", "Group 2", "Group 3"])
    h2s_ppb = st.number_input("H2S Concentration (ppb)", min_value=0.0)
    ch3sh_ppb = st.number_input("CH3SH Concentration (ppb)", min_value=0.0)
    vsc_ppb = st.number_input("VSC Concentration (ppb)", min_value=0.0)
    tongue_coating = st.slider("Tongue Coating Score", min_value=0, max_value=10)
    ratio_ppb = st.number_input("Ratio ppb", min_value=0.0)

    if st.button("Predict Halitosis"):
        st.info("Prediction feature not implemented in demo.")

# 5th Interface: Final Results & Recommendations
elif page == "Final Results":
    st.title("Final Prediction Results")

    st.subheader("Prediction Summary")
    
    # Display result based on family history
    if "family_history" in locals() and family_history == 1:
        st.error("You have a high risk of Oral Cancer. Immediate consultation with a specialist is recommended.")
    else:
        st.success("You do not appear to have Oral Cancer based on family history.")

    # Display Uploaded Image
    if "uploaded_file" in locals() and uploaded_file is not None:
        st.image(image, caption="Uploaded Oral Image", use_column_width=True)

    # Recommendations
    st.subheader("Precautions & Recommendations")
    st.write("""
    - Avoid tobacco and alcohol
    - Maintain good oral hygiene
    - Regular dental check-ups
    - Eat a healthy, balanced diet
    - Stay hydrated
    
    If you experience persistent symptoms, consult a healthcare professional.
    """)

    # Add a relevant image
    st.image("https://www.cdc.gov/oralhealth/images/OralCancer-1200x675.jpg", use_column_width=True)

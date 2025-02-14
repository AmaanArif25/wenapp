import streamlit as st
import pandas as pd
from PIL import Image

# Set the page config
st.set_page_config(page_title="MUKTA Oral Cancer Detection", page_icon="🦷", layout="wide")

# Load Mukta Logo
mukta_logo = "mukta_logo.png"  # Make sure this file exists in the same directory
st.sidebar.image(mukta_logo, width=200)

# Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["About Oral Cancer- Home", "Oral Cancer Risk Assessment", "Oral Cavity Image for Analysis", "Halitosis Detection", "Final Prediction"])

# 1st Interface: Oral Cancer Awareness
if page == "About Oral Cancer- Home":
    st.title("Understanding Oral Cancer")
    
    # Add a relevant image
    st.image("oralcancerimage.png", caption="Oral Cancer Awareness", use_container_width=True)
    
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
elif page == "Oral Cancer Risk Assessment":
    st.title("Oral Cancer Prediction using Multi-Parametric Data Analysis")

    # User Input Fields
    country = st.text_input("Location")
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    age = st.number_input("Age", min_value=1, max_value=100)
    tobacco_use = st.selectbox("Tobacco Use", ["Yes", "No"])
    alcohol_use = st.selectbox("Alcohol Use", ["Yes", "No"])
    socioeconomic_status = st.selectbox("Socioeconomic Status", ["Low", "Medium", "High"])
    survival_rate = st.slider("Survival Rate (%)", min_value=0, max_value=100)
    hpv_related = st.selectbox("HPV Related", ["No", "Yes"])
    smoking = st.selectbox("Smoking", ["No", "Yes"])
    poor_oral_hygiene = st.selectbox("Poor Oral Hygiene", ["No", "Yes"])
    betel_nut_use = st.selectbox("Betel Nut Use", ["No", "Yes"])
    oral_symptoms = st.text_area("Describe Any other Symptoms present")
    family_history = st.selectbox("Family History of Cancer", ["No", "Yes"])
    if st.button("Predict Cancer Risk"):
        st.session_state["family_history"] = family_history
        st.success("Proceed to the next step!")


# 3rd Interface: Image Upload
elif page == "Oral Cavity Image for Analysis":
    st.title("Upload Oral Cavity Image for Analysis")

    uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)
        st.session_state["uploaded_image"] = uploaded_file
    
    if st.button("Proceed to Halitosis Detection"):
        st.success("Move to the next step!")

# 4th Interface: Halitosis Detection
elif page == "Halitosis Detection":
    st.title("Oral Cancer Prediction using Halitosis data")

    age = st.number_input("Age", min_value=1, max_value=100)
    sex = st.selectbox("Sex", ["Male", "Female", "Other"])
    groups = st.selectbox("Groups", ["Group 1", "Group 2", "Group 3"])
    h2s_ppb = st.number_input("H2S Concentration (ppb)", min_value=0.0)
    ch3sh_ppb = st.number_input("CH3SH Concentration (ppb)", min_value=0.0)
    vsc_ppb = st.number_input("VSC Concentration (ppb)", min_value=0.0)
    tongue_coating = st.slider("Tongue Coating Score", min_value=0, max_value=10)
    ratio_ppb = st.number_input("Ratio ppb", min_value=0.0)

    if st.button("Proceed to Final Prediction"):
        st.success("Move to the final step!")

# 5th Interface: Final Results & Recommendations
elif page == "Final Prediction":
    st.title("Final Cancer Prediction")

    family_history = st.session_state.get("family_history", 0)
    uploaded_image = st.session_state.get("uploaded_image", None)
    
    if family_history == "Yes":
        st.error("The model suggests a HIGH RISK of Oral Cancer. Please consult a doctor immediately.")
    else:
        st.success("The model suggests LOW RISK of Oral Cancer. Stay cautious and maintain good oral hygiene.")
    
    if uploaded_image is not None:
        img = Image.open(uploaded_image)
        st.image(img, caption="User Uploaded Image", use_column_width=True)

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
    st.image("MHCN_Oral cavity_infographic.jpg", use_container_width=True)

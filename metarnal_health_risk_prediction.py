import streamlit as st
import numpy as np
import pickle
import time

# ✅ Load Model
model_path = "Maternal_Health_Dataset.pkl"
try:
    with open(model_path, "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("❌ Model file not found!")
    st.stop()

# ✅ Hospital-Themed UI Styling
st.set_page_config(page_title="Maternal Health Risk", page_icon="🤱", layout="wide")
st.markdown("""
    <style>
    body {background-color: #eafaf1; color: #2c3e50; font-family: 'Poppins', sans-serif;}
    .stButton>button {background-color: #4caf50; color: white; border-radius: 20px; font-size: 18px; padding: 10px 22px;}
    .title {font-size: 48px; font-weight: bold; color: #16a085; text-align: center;}
    .subtitle {font-size: 22px; color: #27ae60; text-align: center; font-style: italic;}
    .about-section {padding: 15px; background-color: #f4f9f4; border-radius: 15px; border-left: 5px solid #2ecc71; margin-bottom: 20px;}
    </style>
    """, unsafe_allow_html=True)

st.markdown("<div class='title'>🤱 Maternal Health Risk Predictor</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>🩺 Providing care through technology</div>", unsafe_allow_html=True)

with st.sidebar:
    st.header("🤱 About Our App")
    st.write("Our mission is to support maternal health with accurate, machine learning-based risk assessments.")
    st.write("This tool provides insights to help expectant mothers and healthcare providers make informed decisions.")
    st.markdown("</div>", unsafe_allow_html=True)
    st.header("💡 Quick Tips")
    st.write("✔️ Enter details accurately for better predictions.")
    st.write("✔️ Use results to consult healthcare providers.")



# ✅ Input Fields
Age = st.slider("👩‍🦰 Age (years)", 18, 45, 25)
SystolicBP = st.number_input("💓 Systolic BP (mm Hg)", value=120.0)
DiastolicBP = st.number_input("💙 Diastolic BP (mm Hg)", value=80.0)
BS = st.number_input("🍬 Blood Sugar Level", value=90.0)
Hemoglobin = st.number_input("🩸 Hemoglobin (g/dL)", value=13.0)
BMI = st.number_input("📊 BMI", value=22.0)
BodyTemp = st.number_input("🌡️ Body Temp (°F)", value=100.0)
HeartRate = st.number_input("❤️ Heart Rate (bpm)", value=70.0)
Parity = st.number_input("🤰 Pregnancies (Parity)", value=0)
SmokingStatus = 1 if st.selectbox("🚬 Smoker?", ['No', 'Yes']) == 'Yes' else 0
PhysicalActivityLevel = {'Low': 0, 'Moderate': 1, 'High': 2}[st.selectbox("🏃 Activity Level", ['Low', 'Moderate', 'High'])]

# ✅ Prediction Outcome with Tips
if st.button("📊 Predict Risk"):
    with st.spinner('⏳ Analyzing health metrics...'):
        time.sleep(2)
        user_input = np.array([[Age, SystolicBP, DiastolicBP, BS, BodyTemp, HeartRate, Hemoglobin, BMI, Parity, SmokingStatus, PhysicalActivityLevel]])
        try:
            prediction = model.predict(user_input)
            if prediction[0] == 2:
                st.error("🚨 High Risk! Urgent medical consultation advised.")
                st.info("💡 Tip: Maintain regular check-ups, manage blood pressure,monitor your sugar levels and avoid smoking.")
            elif prediction[0] == 1:
                st.warning("⚠️ Moderate Risk. Prioritize a healthier lifestyle.")
                st.info("💡 Tip: Increase physical activity, maintain a balanced diet, and monitor your sugar levels.")
            else:
                st.success("✅ Low Risk. Continue maintaining your well-being!")
                st.info("💡 Tip: Stay active, eat healthily, and attend regular health check-ups.")
        except Exception as e:
            st.error(f"❌ Prediction Error: {e}")

st.markdown("---")
st.markdown("👨‍💻 Built with ❤️ by Pratik Gaikwad")

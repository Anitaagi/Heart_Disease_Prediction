import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("heart_model.pkl", "rb"))

st.title("❤️ Heart Disease Prediction App")
st.markdown("### Enter patient details to predict heart disease risk")

age = st.slider("Age", 20, 100, 50)
sex = st.selectbox("Sex", ["Male", "Female"])
resting_bp = st.slider("Resting Blood Pressure (mmHg)", 80, 200, 120)
cholesterol = st.slider("Cholesterol (mg/dL)", 100, 600, 200)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120mg/dl", [0, 1])
max_hr = st.slider("Maximum Heart Rate", 60, 220, 150)
oldpeak = st.slider("Oldpeak (ST Depression)", 0.0, 6.0, 1.0)
chest_ATA = st.selectbox("Chest Pain Type ATA", [0, 1])
chest_NAP = st.selectbox("Chest Pain Type NAP", [0, 1])
chest_TA = st.selectbox("Chest Pain Type TA", [0, 1])
resting_ecg_normal = st.selectbox("Resting ECG Normal", [0, 1])
resting_ecg_st = st.selectbox("Resting ECG ST", [0, 1])
exercise_angina = st.selectbox("Exercise Angina", [0, 1])
st_slope_flat = st.selectbox("ST Slope Flat", [0, 1])
st_slope_up = st.selectbox("ST Slope Up", [0, 1])

sex_val = 1 if sex == "Male" else 0

input_data = np.array([[age, sex_val, resting_bp, cholesterol,
                         fasting_bs, max_hr, oldpeak, chest_ATA,
                         chest_NAP, chest_TA, resting_ecg_normal,
                         resting_ecg_st, exercise_angina,
                         st_slope_flat, st_slope_up]])

if st.button("🔍 Predict"):
    result = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1] * 100
    if result == 1:
        st.error(f"⚠️ High risk of Heart Disease detected ({probability:.1f}% probability)")
    else:
        st.success(f"✅ Low risk of Heart Disease ({probability:.1f}% probability)")

st.markdown("---")
st.markdown("*This app is for educational purposes only. Always consult a doctor.*")
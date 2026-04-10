# Heart Disease Prediction App

A machine learning web application that predicts the risk of 
heart disease based on clinical measurements and symptoms.

## 🔗 Live App
[Click here to view the app](https://anitaagi-heart-disease-prediction.streamlit.app/)

## 📊 Project Overview
Heart disease is one of the leading causes of death worldwide. 
Early detection can save lives. This project uses machine learning 
to predict whether a patient is at risk of heart disease based on 
clinical data collected during medical examinations.

## 🎯 Model Performance
- **Algorithm:** Random Forest Classifier
- **Accuracy:** 86.96%
- **True Positive Rate:** 94/107 disease cases correctly detected

## 📁 Dataset
- **Source:** Heart Disease Dataset (Kaggle/UCI)
- **Size:** 918 patient records
- **Target:** HeartDisease (0 = No Disease, 1 = Disease)

## 🔍 Key Features Used
| Feature | Description |
|---|---|
| Age | Patient age in years |
| Sex | Male or Female |
| RestingBP | Resting blood pressure (mmHg) |
| Cholesterol | Serum cholesterol (mg/dL) |
| FastingBS | Fasting blood sugar > 120mg/dl |
| MaxHR | Maximum heart rate achieved |
| Oldpeak | ST depression during exercise |
| ChestPainType | Type of chest pain experienced |
| RestingECG | Resting ECG results |
| ExerciseAngina | Exercise induced angina |
| ST_Slope | Slope of peak exercise ST segment |

## 📈 Key Findings from EDA
- **ST_Slope_Flat** has the strongest positive correlation (0.55) 
  with heart disease
- **ExerciseAngina** strongly indicates disease risk (0.49)
- **MaxHR** negatively correlates (-0.4) — lower max heart rate 
  means higher risk
- **Oldpeak** positively correlates (0.4) — higher ST depression 
  means higher risk
- **ChestPainType_ATA** negatively correlates (-0.4) — atypical 
  angina patients are less likely to have heart disease
- Asymptomatic patients carry the highest disease risk

## 🛠️ Tech Stack
- **Python** — Core programming language
- **Pandas & NumPy** — Data manipulation
- **Matplotlib & Seaborn** — Data visualization
- **Scikit-learn** — Machine learning
- **Streamlit** — Web application framework
- **Jupyter Notebook** — Development environment

## 📂 Project Structure
Heart_Disease_Prediction/
├── HeartDiseaseApp.ipynb  # Main notebook with analysis
├── app.py                 # Streamlit web application
├── heart_model.pkl        # Trained ML model
├── columns.pkl            # Feature columns
├── heart.csv              # Dataset
├── requirements.txt       # Dependencies
└── README.md              # Project documentation
## 🚀 How to Run Locally
1. Clone the repository
```bash
git clone https://github.com/Anitaagi/Heart_Disease_Prediction.git
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Run the app
```bash
streamlit run app.py
```

## ⚠️ Disclaimer
This app is for educational purposes only. 
Always consult a qualified medical professional for health advice.

## 👤 Author
**Anitaagi**  
Data Science Student  
[GitHub](https://github.com/Anitaagi)

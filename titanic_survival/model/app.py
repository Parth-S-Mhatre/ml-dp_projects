import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load('xgb_titanic_model.pkl')

# Set up the page
st.set_page_config(page_title="🚢 Titanic Survival Predictor", layout="centered")
st.title("🎯 Titanic Survival Prediction Simulator(BETA Version 0.1)")
st.write("Enter passenger details to simulate and predict their chances of survival.")

# --- Input UI ---
pclass = st.selectbox("Passenger Class (1 = Upper, 2 = Middle, 3 = Lower)", [1, 2, 3])
sex = st.radio("Sex", ["Male", "Female"])
sex_encoded = 1 if sex == "Male" else 0

age = st.slider("Age", 1, 80, 25)
sibsp = st.number_input("Number of Siblings/Spouses Aboard (SibSp)", 0, 10, 0)
parch = st.number_input("Number of Parents/Children Aboard (Parch)", 0, 10, 0)
fare = st.slider("Fare Paid (in ₹)", 0.0, 600.0, 32.2)

embarked = st.selectbox("Port of Embarkation", ["Southampton (S)", "Cherbourg (C)", "Queenstown (Q)"])
embarked_encoded = {"Southampton (S)": 2, "Cherbourg (C)": 0, "Queenstown (Q)": 1}[embarked]

# --- Combine features ---
features = np.array([[pclass, sex_encoded, age, sibsp, parch, fare, embarked_encoded]])

# --- Predict on button click ---
if st.button("🧠 Predict Survival"):
    proba = model.predict_proba(features)[0]
    prediction = model.predict(features)[0]

    st.subheader("🧾 Prediction Result")

    if prediction == 1:
        st.success("🟢 The passenger is likely to **SURVIVE!** 🎉")
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMnEyMzVtbGUwbTE0ZmswMmlhNmw2ZDJ3am01enhsdzNqMHJyZHh1NyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/LY1DH1AMbG0tq/giphy.gif", width=350)
    else:
        st.error("🔴 The passenger is likely to **NOT survive.** ☠️")
        st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMGx5cDd0dnQwanpla2ZpanNvZ2hpbG80cWZienk3NmNyNTZ1YWYzeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3orif2yRVSOcd1VuN2/giphy.gif", width=350)

    st.metric("💚 Survival Probability", f"{proba[1]*100:.2f}%")
    st.metric("💀 Non-Survival Probability", f"{proba[0]*100:.2f}%")

# Optional credits
st.caption("Built with ❤️ using Streamlit + XGBoost")
st.caption("As mentioned in the title,this is a BETA version.Please report any bugs or issues ")



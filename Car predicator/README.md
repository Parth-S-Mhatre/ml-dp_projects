# 🚗 Car Price Predictor

A Machine Learning-powered web application that predicts the price of used cars based on vehicle specifications such as company, model, manufacturing year, fuel type, and kilometers driven.

This project demonstrates the complete Machine Learning workflow from data preprocessing and model training to deployment using Flask.

---

## 📌 Project Overview

Buying or selling a used car often involves estimating a fair market price.

This project uses historical used-car data to train a machine learning model capable of predicting car prices based on important vehicle attributes.

The trained model is integrated into a Flask web application that allows users to receive instant price predictions through a simple interface.

---

## 🎯 Objectives

* Perform data cleaning and preprocessing
* Explore relationships between car features and price
* Build a regression model for price prediction
* Deploy the trained model using Flask
* Provide an interactive user interface

---

## 📊 Dataset Information

The project uses a used-car dataset containing information such as:

* Car Name
* Company
* Manufacturing Year
* Fuel Type
* Kilometers Driven
* Selling Price

### Data Cleaning Performed

* Removed invalid records
* Handled missing values
* Converted text-based numerical fields
* Processed categorical variables
* Removed inconsistent pricing entries

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Machine Learning

* Scikit-Learn
* Pandas
* NumPy

### Deployment

* Flask

### Frontend

* HTML
* CSS
* JavaScript

---

## 📂 Project Structure

```text
Car predicator/
│
├── car_predicator.ipynb
├── app.py
├── cleaned_car.csv
├── Linear_model.pkl
│
├── templates/
│   └── index.html
│
└── static/
```

---

## 🔄 Machine Learning Pipeline

```text
Raw Dataset
     │
     ▼
Data Cleaning
     │
     ▼
Feature Engineering
     │
     ▼
Train-Test Split
     │
     ▼
Model Training
     │
     ▼
Model Evaluation
     │
     ▼
Model Serialization
     │
     ▼
Flask Deployment
```

---

## 🤖 Model Used

### Linear Regression

The model learns the relationship between:

* Company
* Model Name
* Manufacturing Year
* Fuel Type
* Kilometers Driven

and predicts:

* Car Price

---

## 🚀 Running the Project

### Clone Repository

```bash
git clone <repository-url>
```

### Install Dependencies

```bash
pip install flask pandas numpy scikit-learn
```

### Run Application

```bash
python app.py
```

### Open Browser

```text
http://localhost:5000
```

---

## 📈 Features

✅ Used car price prediction

✅ Interactive web interface

✅ Data preprocessing pipeline

✅ Machine learning integration

✅ Flask deployment

---

## 🎓 Key Learnings

Through this project I learned:

* Data cleaning techniques
* Feature engineering
* Regression algorithms
* Model serialization using Pickle
* Flask web development
* Integrating ML models with web applications

---

## 🔮 Future Improvements

* XGBoost implementation
* Random Forest comparison
* Confidence interval prediction
* Cloud deployment
* Better UI/UX
* Real-time market data integration

---

## 👨‍💻 Author

**Parth Sanjay Mhatre**

Machine Learning Engineer | AI Enthusiast

📧 [parth.mhatre4141@gmail.com](mailto:parth.mhatre4141@gmail.com)

💼 LinkedIn:
https://www.linkedin.com/in/parthmhatre41/

📸 Instagram:
https://www.instagram.com/parth_s_mhatre/

---

⭐ If you found this project useful, consider giving it a star.

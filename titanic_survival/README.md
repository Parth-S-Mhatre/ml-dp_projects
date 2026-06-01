# 🚢 Titanic Survival Prediction

A Machine Learning project that predicts whether a passenger would survive the Titanic disaster based on passenger information such as age, gender, ticket class, fare, and family relationships.

This project demonstrates the complete machine learning workflow, including exploratory data analysis, feature engineering, model training, model evaluation, and prediction.

---

## 📌 Project Overview

The sinking of the RMS Titanic is one of the most well-known maritime disasters in history.

Using passenger information collected from the Titanic dataset, this project aims to build predictive models capable of determining the likelihood of passenger survival.

The project focuses on understanding how factors such as age, gender, ticket class, fare, and family size influenced survival outcomes.

---

## 🎯 Objectives

* Analyze the Titanic dataset
* Perform Exploratory Data Analysis (EDA)
* Clean and preprocess data
* Engineer meaningful features
* Compare multiple machine learning models
* Predict passenger survival probability
* Evaluate model performance

---

## 📂 Project Structure

```text
titanic_survival/
│
├── notebooks/
│   ├── EDA.ipynb
│   ├── Feature_Engineering.ipynb
│   └── Model_Training.ipynb
│
├── src/
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   └── prediction.py
│
├── model/
│   └── trained_models.pkl
│
├── data/
│
└── README.md
```

---

## 📊 Dataset Information

### Source

Titanic Passenger Dataset

### Features

* Passenger Class (Pclass)
* Name
* Gender (Sex)
* Age
* SibSp (Siblings / Spouses)
* Parch (Parents / Children)
* Ticket Number
* Fare
* Cabin
* Embarked Port

### Target Variable

```text
Survived
```

* 1 → Survived
* 0 → Did Not Survive

---

## 🔍 Exploratory Data Analysis

The project explores:

### Survival Distribution

* Overall survival rate
* Class-wise survival rate
* Gender-wise survival rate

### Feature Analysis

* Passenger Age Distribution
* Fare Distribution
* Family Size Analysis
* Embarkation Port Analysis

### Visualizations

* Histograms
* Count Plots
* Correlation Heatmaps
* Survival Comparison Charts

---

## ⚙️ Data Preprocessing

### Missing Value Handling

* Age Imputation
* Embarked Value Handling
* Cabin Feature Treatment

### Encoding

* Gender Encoding
* Embarked Encoding

### Scaling

* Numerical Feature Standardization

---

## 🛠️ Feature Engineering

Several new features were created to improve model performance.

### Family Size

```text
FamilySize = SibSp + Parch + 1
```

### IsAlone

```text
IsAlone = 1 if FamilySize == 1
```

### Age Groups

Passengers grouped into meaningful age categories.

### Fare Categories

Fare values transformed into ranges.

---

## 🤖 Machine Learning Models

Multiple algorithms were evaluated and compared.

### Logistic Regression

* Simple and interpretable
* Strong baseline model

### Random Forest

* Handles complex relationships
* Provides feature importance

### Gradient Boosting

* Improved predictive performance

### XGBoost (Optional)

* Advanced ensemble learning

---

## 📈 Model Evaluation

Performance was evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix
* Cross Validation

### Model Comparison

| Model               | Purpose            |
| ------------------- | ------------------ |
| Logistic Regression | Baseline           |
| Random Forest       | Feature Importance |
| Gradient Boosting   | Improved Accuracy  |
| XGBoost             | Advanced Ensemble  |

---

## 🔄 Machine Learning Workflow

```text
Titanic Dataset
       │
       ▼
Data Cleaning
       │
       ▼
EDA
       │
       ▼
Feature Engineering
       │
       ▼
Encoding & Scaling
       │
       ▼
Model Training
       │
       ▼
Model Evaluation
       │
       ▼
Prediction
```

---

## 🚀 How to Run

### Clone Repository

```bash
git clone <repository-url>
```

### Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### Launch Jupyter Notebook

```bash
jupyter notebook
```

### Run Notebooks

Open:

```text
notebooks/
```

and execute the notebooks sequentially.

---

## 📊 Key Insights

Some important observations discovered during analysis:

### Gender Impact

Female passengers had significantly higher survival rates compared to male passengers.

### Passenger Class

First-class passengers had a greater chance of survival than passengers in lower classes.

### Family Size

Passengers traveling alone often had different survival outcomes compared to families.

### Fare Influence

Higher fare-paying passengers generally showed better survival rates.

---

## 💡 Key Learnings

This project helped develop skills in:

* Exploratory Data Analysis
* Data Cleaning
* Feature Engineering
* Classification Algorithms
* Model Comparison
* Machine Learning Evaluation
* End-to-End ML Pipelines

---

## 🔮 Future Improvements

* Interactive Streamlit Application
* Survival Probability Dashboard
* Explainable AI (SHAP Analysis)
* Hyperparameter Optimization
* Automated ML Pipeline
* Cloud Deployment

---

## 🎓 Educational Value

This project is an excellent example of a complete supervised machine learning workflow and is widely regarded as one of the foundational datasets for learning predictive analytics.

---

## 👨‍💻 Author

**Parth Sanjay Mhatre**

Machine Learning Engineer | AI Enthusiast | Backend Developer

📧 [parth.mhatre4141@gmail.com](mailto:parth.mhatre4141@gmail.com)

💼 LinkedIn:
https://www.linkedin.com/in/parthmhatre41/

📸 Instagram:
https://www.instagram.com/parth_s_mhatre/

---

⭐ If you found this project useful, consider giving it a star.

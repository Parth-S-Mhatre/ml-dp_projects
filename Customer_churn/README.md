# 👥 Customer Churn Prediction

A Machine Learning project focused on identifying customers who are likely to discontinue a service. The project combines exploratory data analysis, feature engineering, and classification algorithms to help businesses improve customer retention and reduce revenue loss.

---

## 📌 Project Overview

Customer churn is one of the most important challenges faced by subscription-based businesses such as telecom companies, SaaS providers, banks, and streaming services.

This project analyzes customer behavior patterns and predicts whether a customer is likely to leave the service based on historical customer data.

The insights generated from the model can help organizations proactively engage at-risk customers and improve retention strategies.

---

## 🎯 Objectives

* Understand customer behavior through data analysis
* Identify factors contributing to customer churn
* Build predictive classification models
* Compare multiple machine learning algorithms
* Generate business insights from model predictions

---

## 📂 Project Structure

```text
Customer_churn/
│
├── EDA/
│   └── Data_cleaning.ipynb
│
├── Model/
│   └── model_initializations.ipynb
│
└── README.md
```

---

## 📊 Dataset Overview

The dataset contains customer-related information including:

* Customer Demographics
* Service Usage
* Account Information
* Subscription Details
* Billing Information
* Customer Retention Status

### Target Variable

```text
Churn
```

* 1 → Customer Left
* 0 → Customer Retained

---

## 🔍 Exploratory Data Analysis (EDA)

The EDA phase focuses on understanding:

### Data Quality Checks

* Missing Values
* Duplicate Records
* Data Types
* Outliers

### Statistical Analysis

* Customer Distribution
* Churn Distribution
* Correlation Analysis
* Feature Relationships

### Visualizations

* Churn Rate Analysis
* Feature Distributions
* Correlation Heatmaps
* Customer Segmentation Charts

---

## ⚙️ Data Preprocessing

The preprocessing pipeline includes:

* Missing Value Handling
* Categorical Encoding
* Feature Scaling
* Feature Selection
* Train-Test Splitting

---

## 🤖 Machine Learning Models

Various classification algorithms can be evaluated, including:

### Logistic Regression

* Fast and interpretable
* Strong baseline model

### Random Forest

* Handles non-linear relationships
* Feature importance analysis

### Support Vector Machine (SVM)

* Effective for classification tasks
* Robust decision boundaries

### Gradient Boosting

* High predictive performance
* Handles complex patterns

### K-Nearest Neighbors (KNN)

* Simple distance-based classifier

---

## 📈 Evaluation Metrics

Models are evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC Score
* Confusion Matrix

---

## 🧠 Business Impact

Predicting churn enables businesses to:

### Customer Retention

Identify high-risk customers before they leave.

### Targeted Marketing

Offer personalized discounts and incentives.

### Revenue Protection

Reduce customer acquisition costs by retaining existing customers.

### Strategic Decision Making

Understand the factors driving customer dissatisfaction.

---

## 🚀 How to Run

### Clone Repository

```bash
git clone <repository-url>
```

### Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

### Open EDA Notebook

```bash
jupyter notebook EDA/Data_cleaning.ipynb
```

### Open Model Notebook

```bash
jupyter notebook Model/model_initializations.ipynb
```

---

## 🔄 Machine Learning Workflow

```text
Raw Dataset
     │
     ▼
Data Cleaning
     │
     ▼
Exploratory Data Analysis
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
Business Insights
```

---

## 💡 Key Learnings

This project helped strengthen skills in:

* Data Cleaning
* Exploratory Data Analysis
* Customer Analytics
* Classification Algorithms
* Feature Engineering
* Model Evaluation
* Business-Oriented Machine Learning

---

## 🔮 Future Improvements

* Hyperparameter Optimization
* Ensemble Learning Techniques
* XGBoost & LightGBM Models
* Model Deployment with Flask/FastAPI
* Interactive Dashboard
* Customer Retention Recommendation System

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

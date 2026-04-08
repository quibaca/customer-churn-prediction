# customer-churn-prediction
End-to-end Customer Churn Prediction project using Machine Learning, with data analysis, predictive modeling, and interactive dashboards built in Streamlit and Power BI.

# 📊 Customer Churn Prediction

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![Dashboard](https://img.shields.io/badge/Dashboard-Streamlit-red)
![BI](https://img.shields.io/badge/PowerBI-Analytics-yellow)

---

##  Overview
This is an end-to-end Machine Learning project designed to predict customer churn.

It combines **data analysis, predictive modeling, and business intelligence dashboards** to identify customers at risk of leaving and support retention strategies.

---

##  Business Problem
Customer churn is a critical issue for subscription-based companies.

👉 Key questions:
- Which customers are likely to churn?
- What factors drive customer churn?
- How can businesses reduce churn?

---

##  Machine Learning Pipeline

### 🔹 Data Processing
- Data cleaning
- Feature engineering
- Categorical encoding

### 🔹 Model
- Logistic Regression

### 🔹 Evaluation
- Accuracy
- Precision
- Recall
- F1-score

---

##  Key Insights

-  Customers with **month-to-month contracts** have higher churn rates  
-  Higher **monthly charges** increase churn risk  
-  Lack of **tech support** is strongly linked to churn  
-  Long-term contracts significantly reduce churn  

---

##  Dashboards

###  Streamlit App
- Interactive prediction interface
- Real-time churn probability
- User-friendly inputs

###  Power BI Dashboard
- Customer segmentation
- Churn trends
- Business insights

---

##  Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit
- Power BI
- Matplotlib / Seaborn

---

##  How to Run

```bash
git clone https://github.com/YOUR-USERNAME/customer-churn-prediction.git
cd customer-churn-prediction

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

streamlit run dashboard/dashboard.py
```

customer-churn-prediction/
│
├── dashboard/
├── data/
├── model/
├── notebooks/
├── src/
│
├── requirements.txt
└── README.md



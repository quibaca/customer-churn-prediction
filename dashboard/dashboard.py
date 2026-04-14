import streamlit as st
import pandas as pd
import joblib


model = joblib.load("model/churn_model.pkl")
model_columns = joblib.load("model/model_columns.pkl")

st.title("Customer Churn Prediction")
st.write("Enter customer information")
tenure = st.number_input("Tenure (months)", 0, 72)
monthly_charges = st.number_input("Monthly Charges", 0.0, 200.0)
contract = st.selectbox(
    "Contract Type",
    ["Month-to-month", "One year", "Two year"]
)

internet_service = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)
tech_support = st.selectbox(
    "Tech Support",
    ["Yes", "No"]
)
partner = st.selectbox(
    "Partner",
    ["Yes", "No"]
)
dependents = st.selectbox(
    "Dependents",
    ["Yes", "No"]
)
contract_one = 0
contract_two = 0

if contract == "One year":
    contract_one = 1

elif contract == "Two year":
    contract_two = 1

internet_dsl = 0
internet_fiber = 0

if internet_service == "DSL":
    internet_dsl = 1

elif internet_service == "Fiber optic":
    internet_fiber = 1



tech_support_yes = 1 if tech_support == "Yes" else 0
partner_yes = 1 if partner == "Yes" else 0
dependents_yes = 1 if dependents == "Yes" else 0

data = pd.DataFrame({
    
    "tenure":[tenure],
    "MonthlyCharges":[monthly_charges],
    "Contract_One year":[contract_one],
    "Contract_Two year":[contract_two],
    "InternetService_DSL":[internet_dsl],
    "InternetService_Fiber optic":[internet_fiber],
    "TechSupport_Yes":[tech_support_yes],
    "Partner_Yes":[partner_yes],
    "Dependents_Yes":[dependents_yes]

})

data = data.reindex(columns=model_columns, fill_value=0)
if st.button("Predict Churn"):

    prediction = model.predict(data)
    probability = model.predict_proba(data)[0][1]
    st.write("Churn probability:", round(probability*100,2), "%")
    if prediction[0] == 1:

        st.error("⚠ Customer likely to churn")
    else:

        st.success(" Customer likely to stay")
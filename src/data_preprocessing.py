import pandas as pd
from sklearn.model_selection import train_test_split


df = pd.read_csv("data/Telco_Customer_Churn_Dataset.csv")


df = df.drop(columns=["customerID"])

df["Churn"] = df["Churn"].map({"Yes":1, "No":0})


df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

df = df.dropna()

df = pd.get_dummies(df, drop_first=True)

x = df.drop("Churn", axis=1)
y = df["Churn"]


x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

print("X train:", x_train.shape)
print("X test:", x_test.shape)
print("Y train:", y_train.shape)
print("Y test:", y_test.shape)
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

from data_preprocessing import x_train, x_test, y_train, y_test

model = LogisticRegression(max_iter = 2000)

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
print(classification_report(y_test, y_pred))

joblib.dump(model, "model/churn_model.pkl")
joblib.dump(x_train.columns, "model/model_columns.pkl")

print("Model Saved! ")


importance = pd.DataFrame({
    "Feature": x_train.columns,
    "Importance": model.coef_[0]
})

importance = importance.sort_values(by="Importance", ascending=False)

print(importance)
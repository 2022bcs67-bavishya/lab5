import pandas as pd
import json
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# Load dataset
data = pd.read_csv("dataset/winequality-red.csv", sep=";")

X = data.drop("quality", axis=1)
y = data["quality"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

import os

# Create app/artifacts directory if it doesn't exist
os.makedirs("app/artifacts", exist_ok=True)

# Save model
with open("app/artifacts/model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save metrics (using r2 as accuracy for comparison)
metrics = {
    "mse": mse,
    "r2": r2,
    "accuracy": r2  # Using r2 as accuracy for Jenkins comparison
}

with open("app/artifacts/metrics.json", "w") as f:
    json.dump(metrics, f)

print(metrics)

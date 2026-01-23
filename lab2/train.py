import pandas as pd
import json
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.pipeline import Pipeline
import os
import sys

# Get experiment configuration from environment variables
experiment_name = os.getenv("EXPERIMENT_NAME", "Experiment 1")
model_type = os.getenv("MODEL_TYPE", "random_forest")
n_estimators = int(os.getenv("N_ESTIMATORS", "100"))
max_depth = int(os.getenv("MAX_DEPTH", "15"))
test_size = float(os.getenv("TEST_SIZE", "0.3"))
alpha = float(os.getenv("ALPHA", "1.0"))

# Load dataset
df = pd.read_csv("data/winequality-red.csv", sep=";")

X = df.drop("quality", axis=1)
y = df["quality"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=test_size, random_state=42
)

# Create model based on type
if model_type == "random_forest":
    model = RandomForestRegressor(
        n_estimators=n_estimators,
        max_depth=max_depth,
        random_state=42
    )
elif model_type == "ridge":
    model = Ridge(alpha=alpha, random_state=42)
else:
    raise ValueError(f"Unknown model type: {model_type}")

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Experiment: {experiment_name}")
print(f"Model Type: {model_type}")
print(f"MSE: {mse}")
print(f"R2 Score: {r2}")

# Save outputs
os.makedirs("outputs", exist_ok=True)

joblib.dump(model, f"outputs/model_{experiment_name.replace(' ', '_').lower()}.pkl")

results = {
    "experiment_name": experiment_name,
    "model_type": model_type,
    "MSE": mse,
    "R2": r2,
    "parameters": {
        "n_estimators": n_estimators if model_type == "random_forest" else None,
        "max_depth": max_depth if model_type == "random_forest" else None,
        "alpha": alpha if model_type == "ridge" else None,
        "test_size": test_size
    }
}

with open(f"outputs/results_{experiment_name.replace(' ', '_').lower()}.json", "w") as f:
    json.dump(results, f, indent=4)

# Write metrics to GitHub Actions Job Summary
github_summary = os.getenv("GITHUB_STEP_SUMMARY")

if github_summary:
    with open(github_summary, "a") as f:
        f.write(f"## {experiment_name}\n")
        f.write("**Name:** Bavishya  \n")
        f.write("**Roll No:** 2022BCS0067  \n\n")
        f.write(f"**Model Type:** {model_type}\n")
        if model_type == "random_forest":
            f.write(f"**Parameters:** n_estimators={n_estimators}, max_depth={max_depth}, test_size={test_size}\n\n")
        elif model_type == "ridge":
            f.write(f"**Parameters:** alpha={alpha}, test_size={test_size}\n\n")
        f.write(f"- **MSE:** {mse:.6f}\n")
        f.write(f"- **R2 Score:** {r2:.6f}\n\n")
        f.write("---\n\n")

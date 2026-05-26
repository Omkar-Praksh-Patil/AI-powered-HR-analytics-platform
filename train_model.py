"""
train_model.py
--------------
Trains a Random Forest classifier on the cleaned employee dataset
and saves the model as employee_model.pkl.

Run this script BEFORE starting the Flask app:
    python train_model.py

Requirements:
    - employee_cleaned.csv must exist (run clean_data.py first)
"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pickle

# ── Load cleaned dataset ──────────────────────────────────────────────────────
df = pd.read_csv("employee_cleaned.csv")

# ── Features & Target ─────────────────────────────────────────────────────────
X = df[["Age", "TotalWorkingYears", "MonthlyIncome", "JobSatisfaction"]]
y = df["Attrition"]

# ── Train / Test Split ────────────────────────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ── Train Model ───────────────────────────────────────────────────────────────
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ── Evaluate ──────────────────────────────────────────────────────────────────
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"✅ Model trained successfully!")
print(f"📊 Accuracy: {accuracy * 100:.2f}%")
print()
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=["Stay", "Leave"]))

# ── Save Model ────────────────────────────────────────────────────────────────
with open("employee_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("💾 Model saved to employee_model.pkl")

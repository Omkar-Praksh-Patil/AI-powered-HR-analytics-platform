from flask import Flask, render_template, request
import pickle
import numpy as np
from pymongo import MongoClient
from datetime import datetime
import time

app = Flask(__name__)

# 🔹 Load ML model
model = pickle.load(open("employee_model.pkl", "rb"))

# 🔹 MongoDB connection
try:
    client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=2000)
    client.server_info()  # trigger connection test
    db = client["employee_db"]
    collection = db["predictions"]
    MONGO_AVAILABLE = True
except Exception:
    print("Warning: MongoDB is not available. Using in-memory fallback for predictions.")
    MONGO_AVAILABLE = False
    in_memory_predictions = []

# 🔹 Home page (Prediction)
@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    prob = None
    risk = ""

    if request.method == "POST":
        try:
            age = float(request.form["age"])
            experience = float(request.form["experience"])
            income = float(request.form["income"])
            satisfaction = float(request.form["satisfaction"])

            input_data = np.array([[age, experience, income, satisfaction]])

            # Add a short delay so the loading animation is visible to users.
            time.sleep(1.4)

            # 🔹 Prediction
            prediction = model.predict(input_data)[0]

            # 🔹 Probability
            prob = model.predict_proba(input_data)[0][1]

            # 🔹 Risk classification
            if prob > 0.7:
                risk = "High Risk ⚠️"
            elif prob > 0.3:
                risk = "Medium Risk"
            else:
                risk = "Low Risk"

            # 🔹 Result text
            if prediction == 1:
                result = "Employee likely to leave ❌"
            else:
                result = "Employee will stay ✅"

            # 🔹 Save to MongoDB or Fallback
            doc = {
                "age": age,
                "experience": experience,
                "income": income,
                "satisfaction": satisfaction,
                "prediction": result,
                "probability": float(prob),
                "risk": risk,
                "timestamp": datetime.now()
            }
            if MONGO_AVAILABLE:
                collection.insert_one(doc)
            else:
                in_memory_predictions.insert(0, doc)


        except Exception as e:
            result = f"Error: {str(e)}"

    return render_template("index.html", result=result, prob=prob, risk=risk)


# 🔹 History page
@app.route("/history")
def history():
    if MONGO_AVAILABLE:
        data = list(collection.find().sort("timestamp", -1))
    else:
        data = in_memory_predictions
    return render_template("history.html", data=data)


# 🔹 Dashboard page (NEW FEATURE)
@app.route("/dashboard")
def dashboard():
    if MONGO_AVAILABLE:
        total = collection.count_documents({})
        high = collection.count_documents({"risk": "High Risk ⚠️"})
        medium = collection.count_documents({"risk": "Medium Risk"})
        low = collection.count_documents({"risk": "Low Risk"})
    else:
        total = len(in_memory_predictions)
        high = sum(1 for p in in_memory_predictions if p["risk"] == "High Risk ⚠️")
        medium = sum(1 for p in in_memory_predictions if p["risk"] == "Medium Risk")
        low = sum(1 for p in in_memory_predictions if p["risk"] == "Low Risk")

    return render_template("dashboard.html",
                           total=total,
                           high=high,
                           medium=medium,
                           low=low)


# 🔹 Run app
if __name__ == "__main__":
    app.run(debug=True)
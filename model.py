from flask import Flask, render_template, request
import pickle
import numpy as np

# Initialize app
app = Flask(__name__)

# Load trained model
model = pickle.load(open("employee_model.pkl", "rb"))

# Home route (website UI + prediction)
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

            prediction = model.predict(input_data)[0]
            prob = model.predict_proba(input_data)[0][1]

            if prob > 0.7:
                risk = "High Risk ⚠️"
            elif prob > 0.3:
                risk = "Medium Risk"
            else:
                risk = "Low Risk"

            if prediction == 1:
                result = "Employee likely to leave ❌"
            else:
                result = "Employee will stay ✅"

        except Exception as e:
            result = f"Error: {str(e)}"

    return render_template("index.html", result=result, prob=prob, risk=risk)


# Run server
if __name__ == "__main__":
    app.run(debug=True)
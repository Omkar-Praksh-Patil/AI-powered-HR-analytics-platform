# 🧠 Inventeron — Employee Attrition Predictor

> An AI-powered HR analytics web application that predicts employee attrition risk using Machine Learning, built with Flask and MongoDB.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0-black?logo=flask)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.4-orange?logo=scikit-learn)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-green?logo=mongodb)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📌 About

**Inventeron** is an enterprise-grade HR analytics platform that uses a trained **Random Forest classifier** to predict whether an employee is likely to leave the organization. HR managers can input employee data and instantly receive a **risk classification** (High / Medium / Low) along with an **attrition probability score**.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔮 **AI Prediction** | Predicts attrition risk using a trained ML model |
| 📊 **Analytics Dashboard** | Visual breakdown of all predictions with Chart.js |
| 📋 **Prediction History** | Full log of all past predictions stored in MongoDB |
| ⚠️ **Risk Classification** | High / Medium / Low risk levels with retention insights |
| 🔄 **MongoDB Fallback** | In-memory fallback if MongoDB is unavailable |
| 📱 **Responsive UI** | Works on desktop and mobile with sidebar navigation |

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **ML Model**: scikit-learn (Random Forest Classifier)
- **Database**: MongoDB (with pymongo)
- **Frontend**: HTML5, Tailwind CSS, Chart.js
- **Dataset**: IBM HR Analytics Employee Attrition dataset

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- MongoDB (optional — app works without it using in-memory storage)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/inventeron.git
cd inventeron

# 2. Create a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# Edit .env with your MongoDB URI if needed
```

### Prepare the Model

```bash
# Step 1: Clean the raw dataset
python clean_data.py

# Step 2: Train and save the ML model
python train_model.py
```

### Run the App

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

## 📂 Project Structure

```
inventeron/
├── app.py               # Main Flask application & routes
├── clean_data.py        # Data preprocessing script
├── train_model.py       # Model training script
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variable template
├── .gitignore           # Git ignore rules
├── templates/
│   ├── index.html       # Prediction form (Home page)
│   ├── history.html     # Prediction history page
│   └── dashboard.html   # Analytics dashboard
└── static/
    └── css/             # Stylesheets
```

---

## 🧬 ML Model Details

| Property | Value |
|----------|-------|
| Algorithm | Random Forest Classifier |
| Features | Age, TotalWorkingYears, MonthlyIncome, JobSatisfaction |
| Target | Attrition (Yes / No) |
| Dataset | IBM HR Analytics (1470 records) |
| Train/Test Split | 80% / 20% |

### Risk Classification Logic

| Probability | Risk Level |
|-------------|-----------|
| > 70% | 🔴 High Risk |
| 30% – 70% | 🟡 Medium Risk |
| < 30% | 🟢 Low Risk |

---

## 📡 API Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET, POST | Home — prediction form |
| `/history` | GET | View all past predictions |
| `/dashboard` | GET | Analytics dashboard |

---

## 🗄️ Database Schema (MongoDB)

Each prediction is stored as a document:

```json
{
  "age": 35,
  "experience": 10,
  "income": 5000,
  "satisfaction": 3,
  "prediction": "Employee will stay ✅",
  "probability": 0.24,
  "risk": "Low Risk",
  "timestamp": "2025-01-01T10:00:00"
}
```

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

**Omkar** — Built as part of the Inventeron HR Analytics platform.

> ⭐ If you found this helpful, please give the repo a star!

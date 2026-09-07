# 🎓 Smart Student Performance Predictor

> An end-to-end Machine Learning project that predicts a student's academic performance score from learning and lifestyle factors.

## ✨ Highlights

- 🤖 Random Forest Regression
- 📊 Data-driven performance prediction
- 🎛️ Interactive Streamlit dashboard
- 📈 Model evaluation with MAE and R²
- 🧠 Six meaningful input features
- 📁 Reproducible dataset included
- ⚡ Model trains automatically when the app starts

## 🛠️ Tech Stack

**Python** · **Pandas** · **NumPy** · **Scikit-learn** · **Streamlit**

## 📁 Project Structure

```text
Smart-Student-Performance-Predictor/
├── app.py
├── train_model.py
├── requirements.txt
├── .gitignore
├── README.md
├── data/
│   └── student_performance.csv
└── models/
    └── metrics.txt
```

## 🚀 Run Locally

```bash
git clone https://github.com/yashwaje712/smart-student-performance-predictor.git
cd smart-student-performance-predictor
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Start the app

```bash
streamlit run app.py
```

## 🧠 How It Works

1. Load the student performance dataset.
2. Select learning and lifestyle features.
3. Train a Random Forest Regression model.
4. Accept user inputs through Streamlit.
5. Predict a performance score from 0–100.
6. Display the result with a simple status indicator.

## 📊 Features Used

| Feature | Description |
|---|---|
| `study_hours` | Study hours per day |
| `attendance` | Attendance percentage |
| `assignments_completed` | Completed assignments |
| `sleep_hours` | Sleep hours per day |
| `previous_score` | Previous academic score |
| `extracurricular_hours` | Extracurricular hours per week |

## 📈 Model Evaluation

The included training script reports **Mean Absolute Error (MAE)** and **R² score** on a held-out test set. The dataset is synthetic and designed for educational demonstration.

## ⚠️ Disclaimer

This project is for learning and portfolio demonstration. Predictions should not be used as official academic decisions.

## 👨‍💻 Author

**Yash Waje** — AI & Data Science Student | Python Developer | ML Enthusiast

GitHub: https://github.com/yashwaje712

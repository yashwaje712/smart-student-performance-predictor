<div align="center">

# 🎓 Smart Student Performance Predictor

### Machine Learning Dashboard for Academic Performance Estimation

**Predict • Analyze • Understand** student performance using learning, attendance, and lifestyle factors.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-F7931E?logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-2ea44f.svg)

</div>

---

## 📌 Overview

**Smart Student Performance Predictor** is an end-to-end Machine Learning project that estimates a student's academic performance score from selected learning and lifestyle factors.

The project combines a **Random Forest Regression** model with an interactive **Streamlit dashboard**, making the machine-learning workflow easy to explore and understand.

> **Educational project:** The dataset is synthetic and the predictions are intended for learning and portfolio demonstration, not official academic evaluation.

---

## ✨ Key Features

- 🤖 **Random Forest Regression** for performance estimation
- 🎯 Interactive student-input dashboard
- 📊 Predicted performance score from **0–100**
- 📈 **MAE and R²** model evaluation
- 🧠 Feature-importance visualization
- 📋 Input summary after prediction
- 📁 Reproducible CSV dataset included
- ⚡ Automatic model training with Streamlit caching
- 🛡️ Basic application error handling
- 💻 Simple local setup for students and developers

---

## 🧠 Machine Learning Workflow

```text
Student Performance Dataset
            │
            ▼
     Feature Selection
            │
            ▼
    Train / Test Split
            │
            ▼
 Random Forest Regression
            │
       ┌────┴────┐
       ▼         ▼
 Model Metrics   Feature Importance
       │         │
       └────┬────┘
            ▼
   Streamlit Prediction UI
            │
            ▼
 Predicted Performance Score
```

---

## 📊 Input Features

| Feature | Description |
|---|---|
| `study_hours` | Study hours per day |
| `attendance` | Attendance percentage |
| `assignments_completed` | Number of completed assignments |
| `sleep_hours` | Sleep hours per day |
| `previous_score` | Previous academic score |
| `extracurricular_hours` | Extracurricular hours per week |
| `performance_score` | Target performance score |

---

## 🖥️ Dashboard

The Streamlit application provides:

1. **Dataset overview** — number of rows and model input features.
2. **Model metrics** — MAE and R² on a held-out test split.
3. **Student input controls** — adjust the six model features.
4. **Prediction result** — view the estimated score and progress indicator.
5. **Feature importance** — understand which inputs were most useful to the trained model.
6. **Input summary** — review the values used for the prediction.

---

## 🛠️ Tech Stack

| Category | Technology |
|---|---|
| Language | Python |
| UI | Streamlit |
| Machine Learning | Scikit-learn |
| Model | Random Forest Regressor |
| Data Processing | Pandas, NumPy |
| Evaluation | MAE, R² |
| Dataset | CSV |
| Version Control | Git + GitHub |

---

## 📁 Project Structure

```text
smart-student-performance-predictor/
│
├── app.py                         # Streamlit dashboard
├── train_model.py                 # Model training & evaluation script
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
├── .gitignore                     # Git exclusions
│
├── data/
│   └── student_performance.csv    # Project dataset
│
└── models/
    └── metrics.txt                # Model evaluation information
```

---

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/yashwaje712/smart-student-performance-predictor.git
cd smart-student-performance-predictor
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate it

**Windows PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the dashboard

```bash
streamlit run app.py
```

The application will open in your browser at the local Streamlit address shown in the terminal.

---

## 🧪 Train the Model Separately

To run the standalone training and evaluation script:

```bash
python train_model.py
```

The script trains the Random Forest model, evaluates it using **Mean Absolute Error (MAE)** and **R²**, and saves the trained model under `models/`.

---

## 📈 Model Evaluation

The training workflow uses an **80/20 train-test split** with a fixed random state for reproducibility.

### Metrics

- **MAE (Mean Absolute Error):** measures the average absolute difference between predicted and actual scores.
- **R² (Coefficient of Determination):** indicates how well the model explains variation in the target values.

Metrics can vary if the dataset or model configuration changes.

---

## 🎯 Example Workflow

```text
1. Start the Streamlit app
        ↓
2. Adjust student learning & lifestyle inputs
        ↓
3. Click "Predict Performance"
        ↓
4. Review predicted score
        ↓
5. Inspect input summary
        ↓
6. Explore feature importance
```

---

## 🎓 Skills Demonstrated

This project demonstrates practical experience with:

- Python programming
- Data preprocessing
- Feature selection
- Supervised Machine Learning
- Regression modeling
- Random Forest algorithms
- Train/test splitting
- Model evaluation
- Pandas and NumPy
- Streamlit application development
- Data visualization
- Git and GitHub project organization

---

## 🔮 Future Improvements

- [ ] Add cross-validation
- [ ] Add hyperparameter tuning
- [ ] Compare Random Forest with Linear Regression and Gradient Boosting
- [ ] Add prediction-history tracking
- [ ] Add richer data visualizations
- [ ] Add explainable-AI insights such as SHAP
- [ ] Add automated tests and CI
- [ ] Deploy the dashboard publicly

---

## ⚠️ Disclaimer

This is an **educational and portfolio project**. The dataset is synthetic, and predictions should not be used as official academic assessments, student grading, admissions decisions, or other high-stakes decisions.

---

## 👨‍💻 Author

<div align="center">

### Yash Waje

**AI & Data Science Student**

Python • Machine Learning • Computer Vision • Deep Learning • Generative AI

⭐ If you find this project useful, consider starring the repository!

</div>

---

<div align="center">

**Build • Learn • Predict • Improve** 🚀

</div>

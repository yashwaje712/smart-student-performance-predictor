<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&height=170&section=header&text=Student%20Performance%20Predictor&fontSize=38&fontColor=E6F7FF&fontAlignY=38&desc=MACHINE%20LEARNING%20%7C%20INTERACTIVE%20DASHBOARD&descAlignY=62&descSize=13&color=0:0B1220,55:102A43,100:0891B2" width="100%" alt="Smart Student Performance Predictor" />

**Explore academic-performance estimation with a Random Forest regression workflow.**

![Python](https://img.shields.io/badge/Python-0B1220?style=flat-square&logo=python&logoColor=67E8F9)
![Streamlit](https://img.shields.io/badge/Streamlit-0B1220?style=flat-square&logo=streamlit&logoColor=67E8F9)
![scikit-learn](https://img.shields.io/badge/scikit--learn-0B1220?style=flat-square&logo=scikitlearn&logoColor=67E8F9)
![Pandas](https://img.shields.io/badge/Pandas-0B1220?style=flat-square&logo=pandas&logoColor=67E8F9)

</div>

---

## Overview

**Smart Student Performance Predictor** is an educational machine-learning project that estimates a performance score from selected learning and lifestyle inputs. It combines a Random Forest regression model with a Streamlit dashboard to make the workflow easy to explore.

> **Important:** The repository documentation describes the dataset as synthetic. Predictions are for learning and demonstration, not official academic evaluation or other high-stakes decisions.

## Features

- Interactive controls for student input features
- Random Forest regression for score estimation
- Prediction score displayed on a 0–100 scale
- Model evaluation using MAE and R²
- Feature-importance visualization
- Input summary after prediction
- Included CSV dataset and a separate training script
- Streamlit caching for the model workflow

## Model workflow

```text
CSV dataset
    │
    ▼
Feature selection and train/test split
    │
    ▼
Random Forest regression
    ├──► Evaluation: MAE and R²
    └──► Feature importance
              │
              ▼
      Streamlit prediction dashboard
```

## Input features

| Feature | Meaning |
|---|---|
| `study_hours` | Study hours per day |
| `attendance` | Attendance percentage |
| `assignments_completed` | Completed assignments |
| `sleep_hours` | Sleep hours per day |
| `previous_score` | Previous score |
| `extracurricular_hours` | Extracurricular hours per week |
| `performance_score` | Target value used by the model |

## Tech stack

| Area | Technology |
|---|---|
| Language | Python |
| Dashboard | Streamlit |
| Model | Random Forest Regressor |
| ML and metrics | scikit-learn, MAE, R² |
| Data processing | Pandas, NumPy |
| Data source | Project CSV dataset |

## Run locally

**Prerequisites:** Python 3.x, Git, and pip.

```bash
git clone https://github.com/yashwaje712/smart-student-performance-predictor.git
cd smart-student-performance-predictor
python -m venv .venv
```

Activate the environment:

**Windows PowerShell**
```powershell
.venv\Scripts\Activate.ps1
```

**macOS / Linux**
```bash
source .venv/bin/activate
```

Install dependencies and run the dashboard:

```bash
pip install -r requirements.txt
streamlit run app.py
```

To run the separate training/evaluation script:

```bash
python train_model.py
```

## Project structure

```text
smart-student-performance-predictor/
├── app.py
├── train_model.py
├── requirements.txt
├── data/
│   └── student_performance.csv
└── models/
    └── metrics.txt
```

## Responsible use

This project is a learning demonstration built around synthetic data. Its estimates do not establish a student's real ability or future outcomes and should not be used for grading, admissions, or other high-stakes decisions.

## Roadmap

- [ ] Cross-validation and hyperparameter tuning
- [ ] Compare multiple regression models
- [ ] Automated tests and continuous integration
- [ ] More explanatory visualizations
- [ ] Public deployment

## Author

**Yash Waje** · [GitHub profile](https://github.com/yashwaje712)

---

<div align="center">

**Explore · Evaluate · Learn**

</div>

from pathlib import Path
import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestRegressor

st.set_page_config(page_title="Smart Student Performance Predictor", page_icon="🎓", layout="centered")

BASE = Path(__file__).parent
DATA_PATH = BASE / "data" / "student_performance.csv"
FEATURES = ["study_hours", "attendance", "assignments_completed", "sleep_hours", "previous_score", "extracurricular_hours"]

@st.cache_resource
def train_model():
    df = pd.read_csv(DATA_PATH)
    model = RandomForestRegressor(n_estimators=200, random_state=42)
    model.fit(df[FEATURES], df["performance_score"])
    return model

model = train_model()

st.title("🎓 Smart Student Performance Predictor")
st.caption("Machine Learning + Streamlit | Predict academic performance from learning factors.")

st.sidebar.header("Student Inputs")
study_hours = st.sidebar.slider("Study hours / day", 1.0, 10.0, 5.0, 0.5)
attendance = st.sidebar.slider("Attendance (%)", 55.0, 100.0, 80.0, 1.0)
assignments = st.sidebar.slider("Assignments completed", 2, 10, 7)
sleep = st.sidebar.slider("Sleep hours / day", 5.0, 9.0, 7.0, 0.5)
previous = st.sidebar.slider("Previous score", 35.0, 95.0, 65.0, 1.0)
extra = st.sidebar.slider("Extracurricular hours / week", 0.0, 8.0, 2.0, 0.5)

if st.button("Predict Performance", type="primary"):
    sample = pd.DataFrame([{
        "study_hours": study_hours,
        "attendance": attendance,
        "assignments_completed": assignments,
        "sleep_hours": sleep,
        "previous_score": previous,
        "extracurricular_hours": extra,
    }])
    score = float(model.predict(sample)[0])
    score = max(0, min(100, score))
    status = "Pass" if score >= 40 else "Needs Improvement"

    st.metric("Predicted Performance Score", f"{score:.1f}/100")
    if status == "Pass":
        st.success(f"Status: {status} ✅")
    else:
        st.warning(f"Status: {status} ⚠️")
    st.progress(score / 100)
    st.info("Educational ML demonstration only — not an official academic assessment.")

st.divider()
st.markdown("### Model Features")
st.write("Study time • Attendance • Assignments • Sleep • Previous score • Extracurricular activity")

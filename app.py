from pathlib import Path

import pandas as pd
import streamlit as st
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

st.set_page_config(
    page_title="Smart Student Performance Predictor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

BASE = Path(__file__).parent
DATA_PATH = BASE / "data" / "student_performance.csv"
FEATURES = [
    "study_hours",
    "attendance",
    "assignments_completed",
    "sleep_hours",
    "previous_score",
    "extracurricular_hours",
]
FEATURE_LABELS = {
    "study_hours": "Study Hours / Day",
    "attendance": "Attendance %",
    "assignments_completed": "Assignments Completed",
    "sleep_hours": "Sleep Hours / Day",
    "previous_score": "Previous Score",
    "extracurricular_hours": "Extracurricular Hours / Week",
}


@st.cache_data
 def load_data():
    return pd.read_csv(DATA_PATH)


@st.cache_resource
 def train_model(data):
    X = data[FEATURES]
    y = data["performance_score"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model = RandomForestRegressor(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    metrics = {
        "mae": mean_absolute_error(y_test, predictions),
        "r2": r2_score(y_test, predictions),
    }
    return model, metrics


try:
    df = load_data()
    model, metrics = train_model(df)
except Exception as exc:
    st.error("Unable to load the project dataset or train the model.")
    st.exception(exc)
    st.stop()

st.title("🎓 Smart Student Performance Predictor")
st.markdown(
    "**Machine Learning dashboard** for estimating academic performance from "
    "learning, attendance, and lifestyle factors."
)
st.caption("Educational portfolio project • Random Forest Regression • Streamlit")

st.divider()

# Project overview
m1, m2, m3, m4 = st.columns(4)
m1.metric("Dataset Rows", f"{len(df):,}")
m2.metric("Input Features", len(FEATURES))
m3.metric("MAE", f"{metrics['mae']:.2f}")
m4.metric("R² Score", f"{metrics['r2']:.3f}")

st.divider()

with st.sidebar:
    st.header("🎯 Student Inputs")
    st.caption("Adjust the values and generate a model prediction.")

    study_hours = st.slider("Study hours / day", 1.0, 10.0, 5.0, 0.5)
    attendance = st.slider("Attendance (%)", 55.0, 100.0, 80.0, 1.0)
    assignments = st.slider("Assignments completed", 2, 10, 7)
    sleep = st.slider("Sleep hours / day", 5.0, 9.0, 7.0, 0.5)
    previous = st.slider("Previous score", 35.0, 95.0, 65.0, 1.0)
    extra = st.slider("Extracurricular hours / week", 0.0, 8.0, 2.0, 0.5)

    predict = st.button("🚀 Predict Performance", type="primary", use_container_width=True)

st.subheader("📊 Prediction")

if predict:
    sample = pd.DataFrame(
        [
            {
                "study_hours": study_hours,
                "attendance": attendance,
                "assignments_completed": assignments,
                "sleep_hours": sleep,
                "previous_score": previous,
                "extracurricular_hours": extra,
            }
        ]
    )

    score = float(model.predict(sample)[0])
    score = max(0.0, min(100.0, score))

    c1, c2 = st.columns([1, 2])
    with c1:
        st.metric("Predicted Performance", f"{score:.1f} / 100")
    with c2:
        st.progress(score / 100)
        if score >= 75:
            st.success("Strong predicted performance")
        elif score >= 50:
            st.info("Moderate predicted performance")
        else:
            st.warning("Performance may need improvement")

    st.subheader("🔎 Input Summary")
    display_df = sample.rename(columns=FEATURE_LABELS).T.rename(columns={0: "Value"})
    st.dataframe(display_df, use_container_width=True)
else:
    st.info("Set the student inputs in the sidebar, then click **Predict Performance**.")

st.divider()

left, right = st.columns(2)
with left:
    st.subheader("🧠 Feature Importance")
    importance = pd.DataFrame(
        {
            "Feature": [FEATURE_LABELS[f] for f in FEATURES],
            "Importance": model.feature_importances_,
        }
    ).sort_values("Importance", ascending=False)
    st.bar_chart(importance.set_index("Feature"))

with right:
    st.subheader("📚 Model Features")
    for feature in FEATURES:
        st.write(f"**{FEATURE_LABELS[feature]}**")
    st.caption(
        "Feature importance indicates how useful each input was to this Random Forest model; "
        "it does not prove causation."
    )

st.divider()
st.subheader("📌 About This Project")
st.write(
    "This project demonstrates an end-to-end machine-learning workflow: dataset loading, "
    "feature selection, Random Forest regression, evaluation with MAE and R², and an "
    "interactive Streamlit interface."
)
st.warning(
    "Educational demonstration only. Predictions should not be used as official academic "
    "assessments or decisions."
)

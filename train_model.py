import pickle
from pathlib import Path
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

BASE = Path(__file__).parent
df = pd.read_csv(BASE / "data" / "student_performance.csv")

features = [
    "study_hours", "attendance", "assignments_completed",
    "sleep_hours", "previous_score", "extracurricular_hours"
]
X, y = df[features], df["performance_score"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

pred = model.predict(X_test)
print(f"MAE: {mean_absolute_error(y_test, pred):.2f}")
print(f"R2: {r2_score(y_test, pred):.3f}")

with open(BASE / "models" / "performance_model.pkl", "wb") as f:
    pickle.dump(model, f)

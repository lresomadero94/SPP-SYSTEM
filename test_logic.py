# Offline test of the app's core logic (Streamlit itself is not required)
import pandas as pd, joblib
model = joblib.load("student_model.pkl")
data = pd.read_csv("student_data.csv")
req = list(model.feature_names_in_)

# Test 1: sample CSV -> predictions
sample = data.drop(columns=["G3"]).head(5)
sample.to_csv("sample_prediction_input.csv", index=False)
new = pd.read_csv("sample_prediction_input.csv")
assert [c for c in req if c not in new.columns] == []
pred = model.predict(new[req])
res = new.copy(); res["Prediction"] = ["AT RISK" if v == 1 else "NOT AT RISK" for v in pred]
print("T1 sample predictions:", list(res["Prediction"]))

# Test 2: missing column -> error message
bad = new.drop(columns=["G2", "absences"])
missing = [c for c in req if c not in bad.columns]
print("T2 error message:", "Missing required columns: " + ", ".join(missing))

# Test 3: results CSV
res.to_csv("student_predictions.csv", index=False)
chk = pd.read_csv("student_predictions.csv")
print("T3 results csv:", chk.shape, "has Prediction:", "Prediction" in chk.columns)

# G3 must not be a feature
assert "G3" not in req
print("G3 excluded from features: True; features used:", len(req))

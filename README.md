# Student Performance Prediction System

A classroom prototype that flags students who may be at risk of failing the final Mathematics grade, built for a Data Mining laboratory.

## Problem
Academic risk is often noticed only after poor results. This prototype explores early identification from available student indicators (study time, absences, past failures, G1 and G2).

## Dataset
UCI Machine Learning Repository, *Student Performance* (ID 320), Mathematics records:
https://archive.ics.uci.edu/dataset/320/student+performance

> **Note:** If the UCI download is unavailable, `train_model.py` falls back to the local `student_data.csv`. The CSV bundled in this repository may be synthetic (generated to match the UCI schema) and is for demonstration only.

## Prediction target
`G3 < 10` = **AT RISK** (1); `G3 >= 10` = **NOT AT RISK** (0). `G3` is the target only and is never used as an input feature.

## Technologies
Python 3.10+, pandas, scikit-learn (Random Forest), joblib, Streamlit, Git/GitHub.

## Installation and run
```bash
pip install -r requirements.txt
python train_model.py      # downloads/loads data, trains, saves student_model.pkl
streamlit run app.py       # opens http://localhost:8501
```
In the app, download the sample input CSV, then upload it to see predictions. Results can be downloaded as CSV.

## Limitations
- Trained on one Portuguese secondary-school dataset; it may not generalize to other institutions or populations.
- G1 and G2 are strong predictors, so the model is better at confirming risk than at predicting it early.
- Predictions are not diagnoses and must not be the sole basis for real student decisions.

# Student Performance Prediction: Laboratory Submission

> Note: results below were produced on a **synthetic** dataset that mirrors the UCI Mathematics schema (395 rows, 33 columns), because the UCI download was unavailable in the build environment. Re-run `train_model.py` with internet access to get real-data metrics.

## 1. SAD mini-analysis
| Element | Response |
|---|---|
| Problem statement | Academic risk is usually noticed after poor results. The prototype explores early identification from study time, absences, failures, G1 and G2. |
| Users | Faculty member or academic analyst |
| Inputs | CSV of student attributes and academic indicators (G3 excluded) |
| Process | Validate columns, preprocess, apply trained Random Forest, classify risk |
| Outputs | AT RISK / NOT AT RISK label, at-risk count, downloadable results CSV, evaluation summary |
| Key limitation | Trained on one Portuguese school dataset; may not generalize to other institutions |

## 2. Model evaluation (20% stratified test set, n = 79)
| Class | Precision | Recall | F1 | Support |
|---|---|---|---|---|
| Not at risk | 0.88 | 0.92 | 0.90 | 48 |
| At risk | 0.86 | 0.81 | 0.83 | 31 |

Accuracy: 0.873 (Random Forest, 100 trees, class_weight="balanced", random_state=42).

## 3. Test table
| Test | Expected result | Evidence | Pass? |
|---|---|---|---|
| Run train_model.py | CSV and model files created without errors | `student_model.pkl` saved; accuracy printed | ☑ |
| Run Streamlit app | Dashboard loads in browser | `app.py` compiles; **run `streamlit run app.py` locally and screenshot** | ☐ (verify locally) |
| Upload sample CSV | Predictions displayed | Logic test: 5 rows → 3 AT RISK, 2 NOT AT RISK | ☑ (logic) |
| Upload CSV missing a column | Helpful error message | "Missing required columns: absences, G2" | ☑ (logic) |
| Download results | CSV containing predictions | `student_predictions.csv` has a Prediction column | ☑ (logic) |
| Open GitHub repository | Source files and README visible | **Push and check the URL** | ☐ (verify locally) |

## 4. Reflection
1. **Target and why G3 is excluded.** The target is whether a student is at risk: 1 if the final Mathematics grade G3 is below 10, otherwise 0. G3 is excluded from the features because the target is computed directly from it. Including it would be target leakage: the model would simply read the answer and report an unrealistically high score, then be useless in practice, when G3 isn't yet known.
2. **Recall for "At risk" (0.81).** Of all students who truly are at risk, the model correctly flags about 81%. The remaining ~19% are missed (false negatives). Since the aim is to offer support, missed at-risk students are the costly error, so recall matters more here than overall accuracy.
3. **Different performance at my institution.** The model learned patterns from two Portuguese secondary schools. Grading scales, curriculum, student demographics, school resources and culture differ elsewhere, so the relationships between inputs (e.g., absences, study time) and outcomes may shift. The model should be validated or retrained on local data before use.
4. **Action after an AT RISK prediction.** Treat it as a prompt for a conversation, not a verdict. The faculty member should review the student's actual records, talk with the student, and offer support such as tutoring or consultation. The prediction must not be the sole basis for any decision about the student.

## 5. Submission checklist
1. ☑ SAD mini-analysis
2. ☑ train_model.py and app.py
3. ☑ requirements.txt and README.md
4. ☑ Model evaluation results
5. ☐ Screenshot of the Streamlit dashboard and prediction results (take locally)
6. ☐ GitHub repository URL (after you push)

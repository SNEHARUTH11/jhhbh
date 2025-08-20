import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from preprocess import load_and_preprocess

# --- Load Data ---
X, y = load_and_preprocess()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- Train Model ---
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# --- Predictions ---
y_pred = model.predict(X_test)

# --- Save Predictions ---
df_preds = pd.DataFrame({
    "Actual": y_test,
    "Predicted": y_pred
})
df_preds.to_csv("data/predictions.csv", index=False)

print("✅ Predictions saved to data/predictions.csv")

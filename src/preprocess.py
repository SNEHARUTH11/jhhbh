
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_and_preprocess(path="data/telco_churn.csv"):
    df = pd.read_csv(path)

    # Clean TotalCharges (convert to numeric)
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)

    # Encode categorical columns
    cat_cols = df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))

    X = df.drop("Churn", axis=1)
    y = df["Churn"]
    return X, y

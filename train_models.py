import os
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

data_folder = "cancer_data"
models_folder = "models"
os.makedirs(models_folder, exist_ok=True)

print("📁 Scanning for CSV files...")

for filename in os.listdir(data_folder):
    if filename.endswith(".csv"):
        print(f"\n📄 Processing: {filename}")
        file_path = os.path.join(data_folder, filename)

        try:
            df = pd.read_csv(file_path)

            target_col = None
            for col in df.columns:
                if col.lower() in ["diagnosis", "target", "label", "outcome"]:
                    target_col = col
                    break

            if not target_col:
                print("⚠️ No suitable target column found.")
                continue

            df.dropna(inplace=True)

            X = df.drop(columns=[target_col])
            y = df[target_col]

            for col in X.columns:
                if X[col].dtype == 'object':
                    le = LabelEncoder()
                    X[col] = le.fit_transform(X[col])

            if y.dtype == 'object':
                y = LabelEncoder().fit_transform(y)

            if len(set(y)) != 2:
                print("⚠️ Target is not binary classification. Skipping.")
                continue

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            model = RandomForestClassifier(n_estimators=100, random_state=42)
            model.fit(X_train, y_train)

            model_name = filename.replace(".csv", "_model.pkl")
            joblib.dump(model, os.path.join(models_folder, model_name))
            print(f"✅ Model saved: {model_name}")

        except Exception as e:
            print(f"❌ Error processing {filename}: {e}")

print("\n🎉 All models trained and saved!")

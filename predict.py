import joblib
import numpy as np
import os

def load_model(cancer_type):
    model_path = os.path.join("models", f"{cancer_type.lower()}_model.pkl")
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model not found for {cancer_type}")
    return joblib.load(model_path)

def predict_cancer(cancer_type, symptoms):
    model = load_model(cancer_type)
    symptom_vector = np.array(symptoms).reshape(1, -1)
    prediction = model.predict(symptom_vector)
    return prediction[0]
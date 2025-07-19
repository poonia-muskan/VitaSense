from flask import Flask, render_template, request, redirect
import joblib
import os
import json
import numpy as np

app = Flask(__name__)

MODEL_FOLDER = "models"

GENERIC_FEATURES = [
    "unexplained_weight_loss",
    "persistent_fatigue",
    "persistent_pain",
    "swelling_or_lumps",
    "unexplained_bleeding",
    "changes_in_bowel_or_bladder",
    "persistent_cough_or_hoarseness",
    "difficulty_swallowing",
    "unexplained_fever_or_night_sweats",
    "skin_changes"
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/select-body')
def select_body():
    body_parts = [
        {'id': 'breast', 'name': 'Breast'},
        {'id': 'lungs', 'name': 'Lungs'},
        {'id': 'colon', 'name': 'Colon'},
        {'id': 'skin', 'name': 'Skin'},
        {'id': 'stomach', 'name': 'Stomach'},
        {'id': 'liver', 'name': 'Liver'},
        {'id': 'prostate', 'name': 'Prostate'},
        {'id': 'cervix', 'name': 'Cervix'},
        {'id': 'blood', 'name': 'Blood (Leukemia)'},
        {'id': 'esophagus', 'name': 'Esophagus'},
        {'id': 'kidney', 'name': 'Kidney'},
        {'id': 'pancreas', 'name': 'Pancreas'},
        {'id': 'brain', 'name': 'Brain'},
        {'id': 'bladder', 'name': 'Bladder'},
        {'id': 'ovary', 'name': 'Ovary'},
        {'id': 'other', 'name': 'Other➕'}
    ]
    return render_template('select_body.html', body_parts=body_parts)

@app.route('/questions/<bodypart>', methods=['GET', 'POST'])
def questions_route(bodypart):
    if bodypart.lower() == "other":
        custom_bodypart = request.form.get("custom_bodypart", "Other")
        features = GENERIC_FEATURES

        return render_template(
            'questions.html',
            bodypart="other",
            features=features,
            display_part=custom_bodypart
        )
    
    model_path = os.path.join(MODEL_FOLDER, f"{bodypart.lower()}_cancer_model.pkl")
    if not os.path.exists(model_path):
        return f"No model found for {bodypart}", 404

    model = joblib.load(model_path)

    try:
        features = list(model.feature_names_in_)
    except AttributeError:
        return "Model is missing feature_names_in_ — please retrain using DataFrame.", 500

    return render_template('questions.html', bodypart=bodypart, features=features, display_part=bodypart)

@app.route('/predict', methods=['POST'])
def predict():
    bodypart = request.form.get('bodypart')
    display_part = request.form.get('display_part', bodypart)

    if bodypart.lower() == "other":
        input_vector = []
        for feature in GENERIC_FEATURES:
            value = int(request.form.get(feature, 0))
            input_vector.append(value)
        score = sum(input_vector) / len(GENERIC_FEATURES)

        if score >= 0.6:
            msg = "⚠️ Some signs might need medical attention. Please consult a doctor."
            risk_score = 70
        elif score >= 0.3:
            msg = "⚠️ Some symptoms detected. Monitor and consult if they persist."
            risk_score = 40
        else:
            msg = "✅ No major symptoms detected. Stay healthy!"
            risk_score = 10

        return render_template("result.html", risk=msg, score=risk_score, bodypart=display_part.capitalize())

    # Normal flow with model
    model_path = os.path.join(MODEL_FOLDER, f"{bodypart.lower()}_cancer_model.pkl")

    if not os.path.exists(model_path):
        return f"No model found for {bodypart}", 404

    model = joblib.load(model_path)
    try:
        features = list(model.feature_names_in_)
    except AttributeError:
        return "Model missing feature names. Retrain with a DataFrame.", 500

    input_vector = []
    for feature in features:
        value = int(request.form.get(feature, 0))
        input_vector.append(value)

    input_array = np.array(input_vector).reshape(1, -1)
    prediction = model.predict(input_array)[0]

    if prediction == 1:
        msg = "⚠️ You may be at risk. Please consult a doctor."
        score = 75
    else:
        msg = "✅ You're likely safe, but stay alert and healthy!"
        score = 15

    return render_template("result.html", risk=msg, score=score, bodypart=display_part.capitalize())

@app.route('/custom-input')
def custom_input_page():
    return render_template('custom_input.html')

@app.route('/cancer-videos')
def cancer_videos():
    return render_template("watch_videos.html")

@app.route('/learn-more')
def learn_more():
    return render_template('learn_more.html')

@app.route('/find-doctors', methods=['GET', 'POST'])
def find_doctors():
    doctors = []
    city_input = ""
    cancer_type = ""
    no_doctor_message = None  

    if request.method == 'POST':
        city_input = request.form.get('city', '').lower()
        cancer_type = request.form.get('cancer_type', '').lower()

        with open('data/doctors_data.json', 'r') as f:
            all_doctors = json.load(f)

        for doc in all_doctors:
            city_match = city_input in doc["city"].lower()
            cancer_match = True if not cancer_type else cancer_type in [s.lower() for s in doc.get("speciality", [])]

            if city_match and cancer_match:
                doctors.append(doc)

        if not doctors:
            try:
                with open('data/no_doctor_info.json', 'r') as nf:
                    no_doc_data = json.load(nf)
                    no_doctor_message = no_doc_data.get(city_input, {}).get("message")
            except FileNotFoundError:
                no_doctor_message = None

    return render_template(
        'find_doctors.html',
        doctors=doctors,
        city=city_input,
        cancer_type=cancer_type,
        no_doctor_message=no_doctor_message  
    )

if __name__ == '__main__':
    app.run(debug=True)
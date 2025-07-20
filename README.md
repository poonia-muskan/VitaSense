# Project: VitaSense - Cancer Risk Prediction & Awareness Platform  
### Overview  
The Cancer Risk Detection Web App is a user-friendly platform that allows individuals to assess their risk levels for various types of cancer based on symptoms. In addition to prediction, it serves as an educational hub—providing users with trusted YouTube videos, verified cancer facts, and doctor information across India to help spread awareness and guide users toward early diagnosis and support.

---

### Features  
Symptom-based Prediction
 - Select symptoms from a list for Breast, Lung, Liver, and Stomach cancers
 - Instantly view your estimated cancer risk percentage based on trained ML models

Educational YouTube Videos
 - Watch curated, trusted medical videos about different cancer types and their symptoms

Find Nearby Doctors
 - Search for trusted doctors in capital cities across Indian states and union territories to get real help

Learn More Page
 - Detailed information about multiple types of cancers
 - Common myths vs. truths debunked for awareness
 - Helps users understand symptoms and prevent panic

Simple Dark-Themed UI
 - Basic layout using HTML with embedded CSS and JavaScript
 - Lightweight and easy-to-use, even on low-resource devices

---

### Tech Stack  
Frontend:
 - HTML5 – for structuring the web pages
 - CSS3 – for styling and dark theme design
 - JavaScript – for interactivity and dynamic content

Machine Learning:
 - Pandas – for data manipulation
 - NumPy – for numerical operations
 - scikit-learn – for training classification models (Random Forest)
 - joblib – for saving and loading ML models as .pkl files

Data:
 - 15 separate CSV datasets – containing symptoms related to 15 different cancer types (one per body part)

Backend:
 - Python 3 – primary programming language
 - Flask – micro web framework to handle backend and routing
 - Jinja2 – for rendering dynamic HTML templates

Deployment:
 - Render
   
---

### Screenshots   
<img width="1918" height="911" alt="Screenshot 2025-07-20 092800" src="https://github.com/user-attachments/assets/06418ac5-1428-4bd4-bc6c-ee8b16ab8d4d" />
<img width="1919" height="912" alt="Screenshot 2025-07-20 092847" src="https://github.com/user-attachments/assets/0c44d399-e91e-4da9-b516-9c215811af82" />
<img width="1919" height="908" alt="Screenshot 2025-07-20 092917" src="https://github.com/user-attachments/assets/a8262916-e04d-442f-8bb9-a658ad2aa191" />
<img width="1919" height="912" alt="Screenshot 2025-07-20 093007" src="https://github.com/user-attachments/assets/89b24690-3069-473d-ae4c-8794af918d20" />
<img width="1919" height="911" alt="Screenshot 2025-07-20 093026" src="https://github.com/user-attachments/assets/6c2cfb14-cf16-413e-bdcb-0b4fddd30c3a" />
<img width="1919" height="916" alt="Screenshot 2025-07-20 093130" src="https://github.com/user-attachments/assets/59cb4eff-337c-4615-ae20-446b87843d72" />

---

### Live Demo
- Link 1 -> 🔗 [VitaSense Web App](https://vitasense.onrender.com/)
- Link 2 -> 🔗 [VitaSense Web App](https://vitasense-nxty.onrender.com)

---

### Acknowledgements
 - Inspired by the real need for early cancer detection and awareness
 - ML models trained with publicly available datasets
 - Doctor data compiled for major Indian cities

---

### Run Locally  

```bash
git clone https://github.com/poonia-muskan/VitaSense.git
cd VitaSense
pip install -r requirements.txt
python app.py

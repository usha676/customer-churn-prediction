# Customer Churn Prediction for a Telecom Company

This project predicts whether a telecom customer is likely to churn based on their account and service details.  
It uses **Machine Learning (Random Forest Classifier)** deployed as a **Flask web application**.

---

## Features
- **Preprocessing Pipeline**: Handles missing values, encodes categorical variables, and scales numerical features.
- **Machine Learning Model**: Trained using `RandomForestClassifier` for churn prediction.
- **Web Interface**: Built with Flask and HTML (Jinja templates) for user-friendly input.

---

## Technologies Used
- Python 3
- Flask
- scikit-learn
- Pandas & NumPy
- HTML & Jinja Templates
- Joblib (for saving ML pipeline)

---

## Project Structure
customer-churn-prediction/
│
├── app.py # Flask app
├── models/
│ └── churn_model_pipeline.pkl # Saved ML pipeline
├── templates/
│ └── index.html # Web interface
├── notebooks/
│ ├── 01_eda_visualization.ipynb
│ ├── 02_preprocessing_encoding_featureengineering.ipynb
│ └── 03_model_training_pipeline.ipynb
├── Customer_Churn_Prediction_Report_Usha_Rani.pdf # Detailed project report
└── README.md # Project documentation

yaml
Copy
Edit

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/customer-chur
n-prediction.git
   c-prediction
Install dependencie
s:

bash
Copy
E -r requiremen
ts.txt
Run the Flask app:
it
python app.py
Ope
Author
Usha ranin your browser and go to:

cpp
Copy
Edit
http://127.0.0.1:5000


## Project Structure

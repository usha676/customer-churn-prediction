from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the trained model pipeline
model = joblib.load('models/churn_model_pipeline.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get form inputs
        tenure = float(request.form['tenure'])
        monthly_charges = float(request.form['monthly_charges'])
        total_charges = float(request.form['total_charges'])
        gender = request.form['gender']
        internet_service = request.form['internet_service']
        contract = request.form['contract']
        payment_method = request.form['payment_method']

        # Create a DataFrame with the same structure as training data
        input_data = pd.DataFrame([{
            'tenure': tenure,
            'MonthlyCharges': monthly_charges,
            'TotalCharges': total_charges,
            'gender': gender,
            'InternetService': internet_service,
            'Contract': contract,
            'PaymentMethod': payment_method
        }])

        # Predict
        prediction = model.predict(input_data)[0]
        result = "Churn" if prediction == 1 else "No Churn"
        return render_template('index.html', prediction_text=f"Customer is likely to: {result}")

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
import joblib 
import logging
logging.basicConfig(level=logging.INFO)


app = Flask(__name__)
mongo_client = MongoClient(port=27017)
db = mongo_client["texasSchoolsDB"]

model = None
scaler = None
label_encoder = None

def load_model_scaler_encoder():
    global model, scaler, label_encoder
    if model is None:
        model = tf.keras.models.load_model("models/ISD_Accountability.keras")
    if scaler is None:
        scaler = joblib.load("models/scaler.gz")
    if label_encoder is None:
        label_encoder = joblib.load('models/label_encoder.joblib')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/visualization')
def visualization():
    return render_template('visualization.html')

@app.route('/predict', methods=['POST'])
def predict():
    load_model_scaler_encoder()  # Load all necessary components

    # Extract data from form
    form_data = request.form
    data = [float(form_data.get(key, "0").replace(',', '').replace('%', '')) for key in [
        "total_students", "attendance_rate", "approaches_ela", "meets_ela", "masters_ela",
        "approaches_math", "meets_math", "masters_math", "tested_college", "criterion_college",
        "graduation_rate"
    ]]
    data = np.array([data])  # Convert data into a 2D array for scaling

    try:
        data_scaled = scaler.transform(data)
        prediction = model.predict(data_scaled)
        prediction_index = np.argmax(prediction, axis=1)[0]
        prediction_label = label_encoder.inverse_transform([prediction_index])[0]
        message = f"This school is rated: {prediction_label}"
    except Exception as e:
        logging.error(f"Error in processing the prediction: {str(e)}")
        message = "Error in processing your request. Please try again."
        prediction_label = "Error"

    # Pass data to the template
    return render_template('results.html', prediction=prediction_label, message=message)




if __name__ == '__main__':
    app.run(debug=True)
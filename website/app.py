from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
import joblib 

app = Flask(__name__)
mongo_client = MongoClient(port=27017)
db = mongo_client["texasSchoolsDB"]
scaler = StandardScaler()  # Assuming the scaler is pre-trained and saved
model = None  # Global variable for the model

def load_model_scaler():
    global model, scaler
    if model is None:
        model = tf.keras.models.load_model("models/ISD_Accountability.keras")
    
    scaler = joblib.load("models/scaler.gz")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/visualization')
def visualization():
    return render_template('visualization.html')

@app.route('/datadistrict')
def get_district_data():
    collection = db['DISTRICTS_INFO_2020_21']
    data_cursor = collection.find({}, {'_id': 0})
    data_list = list(data_cursor)
    return jsonify(data_list)


@app.route('/predict', methods=['POST'])
def predict():
    load_model_scaler()  # Ensure the model and scaler are loaded

    # Extract data from form
    form_data = request.form
    data = [form_data.get("total_students", 0), form_data.get("attendance_rate", 0),
            form_data.get("approaches_ela", 0), form_data.get("meets_ela", 0),
            form_data.get("masters_ela", 0), form_data.get("approaches_math", 0),
            form_data.get("meets_math", 0), form_data.get("masters_math", 0),
            form_data.get("tested_college", 0), form_data.get("criterion_college", 0),
            form_data.get("graduation_rate", 0)]
    data = [float(num.replace(',', '').replace('%', '')) for num in data]
    data = np.array([data])  # Convert data into a 2D array for scaling

    # Scale data
    data = scaler.transform(data)

    # Predict using the loaded model
    prediction = np.array([1])  # This might be the output of a model.predict call
    prediction_list = prediction.tolist()  # Convert to list
    prediction_value = prediction[0]

    # Create a message based on the prediction
    message = "This school meets the required accountability standards!" if prediction_list[0] == 1 else "This school does not meet the required accountability standards!"

    # Pass data to the template
    return render_template('results.html', prediction=prediction_value, message=message)

if __name__ == '__main__':
    app.run(debug=True)


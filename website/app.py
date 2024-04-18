from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from pymongo import MongoClient
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
import tensorflow as tf
from tensorflow.keras.metrics import MeanSquaredError, Metric
from tensorflow import keras
from tensorflow.keras import layers

class CustomLayer(keras.layers.Layer):
    def __init__(self, sublayer, **kwargs):
        super().__init__(**kwargs)
        self.sublayer = sublayer

    def call(self, x):
        return self.sublayer(x)

    def get_config(self):
        base_config = super().get_config()
        sublayer_config = keras.saving.serialize_keras_object(self.sublayer)
        return {**base_config, **{"sublayer": sublayer_config}}

    @classmethod
    def from_config(cls, config):
        sublayer_config = config.pop("sublayer")
        sublayer = keras.saving.deserialize_keras_object(sublayer_config)
        return cls(sublayer, **config)


class MSE(Metric):
    def __init__(self, name='mse', **kwargs):
        super(MSE, self).__init__(name=name, **kwargs)
        self.total = self.add_weight(name='total', initializer='zeros')
        self.count = self.add_weight(name='count', initializer='zeros')

    def update_state(self, y_true, y_pred, sample_weight=None):
        error = tf.reduce_mean(tf.square(y_true - y_pred))
        self.total.assign_add(error)
        self.count.assign_add(1)

    def result(self):
        return self.total / self.count

    def reset_states(self):
        self.total.assign(0)
        self.count.assign(0)


app = Flask(__name__)
CORS(app)

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
    client = MongoClient(port=27017)
    db = client["texasSchoolsDB"]
    collection = db['DISTRICTS_INFO_2020_21']
    data_cursor = collection.find({}, {'_id': 0})
    data_list = list(data_cursor)
    return jsonify(data_list)

@app.route('/dataaccountability')
def get_accountability_data():
    client = MongoClient(port=27017)
    db = client["texasSchoolsDB"]
    collection = db['account_ratings22']
    data_cursor = collection.find({}, {'_id': 0})
    data_list = list(data_cursor)
    return jsonify(data_list)

@app.route('/data/staar20_21')
def get_staar20_21_data():
    client = MongoClient(port=27017)
    db = client["texasSchoolsDB"]
    collection = db['staar20_21']
    data_cursor = collection.find({}, {'_id': 0})
    data_list = list(data_cursor)
    return jsonify(data_list)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Extracting form data:
        approaches_grade = request.form['approaches_grade']
        meets_grade = request.form['meets_grade']
        masters_grade = request.form['masters_grade']
        total_students = request.form['total_students']
        attendance_rate = request.form['attendance_rate']
        grad_rate = request.form['grad_rate']
        annual_grads = request.form['annual_grads']

        # Formatting data for the model:
        input_data = pd.DataFrame({
            'approaches_grade': [approaches_grade],
            'meets_grade': [meets_grade],
            'masters_grade': [masters_grade],
            'total_students': [total_students],
            'attendance_rate': [attendance_rate],
            'grad_rate': [grad_rate],
            'annual_grads': [annual_grads]
        })

        # Load the model and predict:
        model = tf.keras.models.load_model("models/ISD_Accountability.h5", custom_objects={'CustomLayer': CustomLayer, 'MSE': MSE})
        predictions = model.predict(input_data)
        return jsonify(predictions.tolist())
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


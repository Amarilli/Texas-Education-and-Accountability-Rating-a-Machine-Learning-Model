from flask import Flask, jsonify, render_template, request, redirect, url_for
from flask_cors import CORS
from pymongo import MongoClient

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
    data_cursor = collection.find({}, {'_id': 0})  # Exclude MongoDB's _id from results
    data_list = list(data_cursor)
    return jsonify(data_list)

@app.route('/dataaccountability')
def get_accountability_data():
    client = MongoClient(port=27017)
    db = client["texasSchoolsDB"]
    collection = db['account_ratings22']
    data_cursor = collection.find({}, {'_id': 0})  # Exclude MongoDB's _id from results
    data_list = list(data_cursor)
    return jsonify(data_list)

@app.route('/predict', methods=['POST'])
def predict():
    # This is for the MACHINE LEARNING MODEL
    data = request.form
    #  data here and perform the prediction
    # For example:
    # result = your_prediction_function(data)
    # For now, let's just return the form data as a JSON to see it's being captured correctly
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)


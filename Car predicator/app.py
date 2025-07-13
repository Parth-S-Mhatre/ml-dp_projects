from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle
import numpy as np


app = Flask(__name__)
car = pd.read_csv('cleaned_car.csv')
model = pickle.load(open('Linear_model.pkl', 'rb'))
@app.route('/')
def index():
    companies = sorted(car['company'].unique())
    year = sorted(car['year'].unique(), reverse=True)
    fuel_type = sorted(car['fuel_type'].unique())
    return render_template('index.html', companies=companies, year=year, fuel_type=fuel_type)

@app.route('/get_models', methods=['POST'])
def get_models():
    company = request.json['company']
    models = sorted(car[car['company'] == company]['name'].unique())
    return jsonify(models)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    company = data['company']
    car_model = data['car_model']
    year = int(data['year'])
    fuel_type = data['fuel_type']
    km_driven = int(data['km_driven'])

    # Build the input like your training dataset
    # NOTE: column order must match training!
    input_df = pd.DataFrame([[car_model, company, year, fuel_type, km_driven]],
                            columns=['name', 'company', 'year', 'fuel_type', 'kms_driven'])

    # One-hot encode or transform if needed — assume your model handles it via pipeline
    prediction = model.predict(input_df)[0]

    return jsonify({'predicted_price': round(prediction, 2)})




if __name__ == '__main__':
    app.run(debug=True)

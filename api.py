from flask import Blueprint, Flask, request, redirect, url_for, flash, jsonify
import joblib

app = Flask(__name__)

@app.before_first_request
def load_model_to_app():
    filename = 'finalized_model.sav'
    app.predictor = joblib.load(filename)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    test = [data['Issue time'], data['Agency'], data['Fine amount'], data['Body Style Code'], data['Color Code']]
    prediction = app.predictor.predict([test])
    return prediction[0]

def main():
    app.run(host='0.0.0.0', port=8000, debug=False)

if __name__ == '__main__':
    main()

from flask import Flask, request, jsonify
from prediction_service.service import PredictionService

app = Flask(__name__)
prediction_service = PredictionService()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    predictions = prediction_service.make_prediction(data)
    return jsonify(predictions)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

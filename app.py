from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/predict")
def predict():
    return jsonify({"valuation": 375000, "confidence": "high"})

if __name__ == "__main__":
    app.run(debug=True)

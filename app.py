from flask import Flask, jsonify
from flask_cors import CORS
import datetime
import json

app = Flask(__name__)
CORS(app)

LOG_FILE = "valuation_log.json"

def log_request(data):
    log_entry = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "data": data
    }
    try:
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(log_entry) + "\n")
    except Exception as e:
        print("Logging failed:", e)

@app.route("/predict")
def predict():
    result = {"valuation": 375000, "confidence": "high"}
    log_request(result)
    return jsonify(result)

@app.route("/logs")
def get_logs():
    try:
        with open(LOG_FILE, "r") as f:
            lines = f.readlines()
            return jsonify([json.loads(line) for line in lines])
    except FileNotFoundError:
        return jsonify([])

if __name__ == "__main__":
    app.run(debug=True)

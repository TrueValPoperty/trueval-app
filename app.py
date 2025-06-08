from flask import Flask, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

AIRTABLE_API_KEY = os.environ.get("AIRTABLE_API_KEY")
BASE_ID = "appShV6ffCc9yxeHF"
TABLE_ID = "tblV4I8VUyfx4JrnF"

def fetch_logs():
    url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_ID}"
    headers = {
        "Authorization": f"Bearer {AIRTABLE_API_KEY}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("records", [])
    else:
        return {"error": response.text}

@app.route("/")
def home():
    return "✅ TrueVal API is live"

@app.route("/logs")
def logs():
    return jsonify(fetch_logs())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

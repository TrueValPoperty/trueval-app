from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

AIRTABLE_API_KEY = "your_airtable_api_key"
BASE_ID = "appShV6ffCc9yxeHF"
TABLE_ID = "tblV4I8VUyfx4JrnF"

def fetch_logs():
    url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_ID}"
    headers = {
        "Authorization": f"Bearer {AIRTABLE_API_KEY}"
    }
    response = requests.get(url, headers=headers)
    return response.json().get("records", [])

@app.route("/logs")
def logs():
    return jsonify(fetch_logs())

if __name__ == "__main__":
    app.run(debug=True)

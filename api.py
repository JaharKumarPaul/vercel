import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the JSON file
try:
    json_path = os.path.join(os.path.dirname(__file__), 'q-vercel-python.json')
    with open(json_path) as file:
        data = json.load(file)
except FileNotFoundError:
    data = {}  # Handle missing JSON file

@app.route('/api', methods=['GET'])
def get_marks():
    try:
        # Get query parameters
        names = request.args.getlist('name')
        if not names:
            return jsonify({"error": "Please provide at least one name"}), 400

        # Fetch marks from data
        marks = [data.get(name, "Name not found") for name in names]
        return jsonify({"marks": marks})
    except Exception as e:
        # Catch any unexpected errors
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

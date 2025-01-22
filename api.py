import json
from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load marks from JSON file
with open("q-vercel-python.json", "r") as file:
    data = json.load(file)  # Assuming data is a list of dictionaries

@app.route('/api', methods=['GET'])
def get_marks():
    # Get names from query parameters
    names = request.args.getlist("name")
    
    # Find marks for the requested names
    result = []
    for name in names:
        # Search the list for the requested name
        student = next((entry for entry in data if entry["name"] == name), None)
        result.append(student["marks"] if student else None)
    
    # Return as JSON response
    return jsonify({"marks": result})

if __name__ == "__main__":
    app.run(debug=True)

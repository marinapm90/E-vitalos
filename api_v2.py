import json

from flask import Flask, jsonify
import requests
from flask import request
from flask_cors import CORS
import re

    
app = Flask(__name__)
CORS(app)



@app.route('/', methods=['GET'])
def get_additives():
    
    with open('./additives.json', 'r') as jsonfile:
        file_data = json.load(jsonfile)
    
    return jsonify(file_data)



@app.route('/additives/<additive>', methods=['GET'])
def additive(additive):
    
    with open('./additives.json', 'r') as jsonfile:
        file_data = json.load(jsonfile)
    
    return jsonify(file_data[additive])


@app.route("/additives/bulk", methods=["POST"])
def bulk_resolve_additives():

    with open('./additives.json', 'r') as jsonfile:
        file_data = json.load(jsonfile)

    text = request.get_json()
    values = [item.replace("-", "") for item in re.findall(r"E-?\d+", str(text))]
    
    result = {}
        
    for value in values:
        result[value] = file_data[value]
        
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
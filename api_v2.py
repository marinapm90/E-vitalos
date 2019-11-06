import json

from flask import Flask, jsonify
import requests
from flask import request
from flask_cors import CORS
import re

    
app = Flask(__name__)
CORS(app)


@app.route("/additives/bulk", methods=["POST"])
def find_text():
    text = request.get_json()
    result = re.findall(r'E-\d+', str(text))
    result_2 = re.findall(r'E\d+', str(text))
    
    values = []
    for value in result:        
        values.append(value)
    for value in result_2:       
        values.append(value)
    for value in values:
        if "E-" in value:
            values = [item.replace('E-','E') for item in values]           
        else:
            return jsonify(values)


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
    
    result = {}
    
    for value in values:
        result[value] = file_data[value]
    
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
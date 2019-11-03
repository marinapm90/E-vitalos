import json

from flask import Flask, jsonify
import requests
from flask import request

    
app = Flask(__name__)



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
    additives_dict = request.get_json()    
    additives = additives_dict["additives"]
    result = {}
    for additive in additives:
        result[additive] = file_data[additive]
    
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
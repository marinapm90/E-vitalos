import json

from flask import Flask, jsonify

    
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

if __name__ == '__main__':
    app.run(debug=True)
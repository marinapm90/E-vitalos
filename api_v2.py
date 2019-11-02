import json

from flask import Flask
    
app = Flask(__name__)


@app.route('/additive/<additive>', methods=['GET'])
def additive(additive):
    
    with open('./additives.json', 'r') as jsonfile:
        file_data = json.loads(jsonfile.read())
    
    return json.dumps(file_data[additive])

if __name__ == '__main__':
    app.run(debug=True)
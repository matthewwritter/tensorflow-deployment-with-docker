from flask import Flask, jsonify, make_response, request, abort
import pickle
from sklearn.linear_model import LogisticRegression
app = Flask(__name__)

def preprocessor(txt):
    return len(txt.split())

@app.route('/')
def hello_world():
    return 'Flask Dockerized EDITED01'

@app.route('/api/ping', methods=['GET'])
def ping():
    return jsonify({'output':[{'a':'b'}, {'c':'d'}]})

@app.route('/api/inference', methods=['POST'])
def inference():
    if not request.json:
        abort(400)
    x = [[preprocessor(request.json['input_txt'])]]
    with open('basic_model.pkl', 'rb') as f:
        lr = pickle.load(f)
    y_pred = lr.predict(x)
    return jsonify({'transformed_input': str(x), 'prediction':str(y_pred)}), 201


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')



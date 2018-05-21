from flask import Flask, jsonify, make_response, request, abort
app = Flask(__name__)

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
    return jsonify({'echo': request.json}), 201


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')



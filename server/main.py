from flask import Flask, request, jsonify, make_response
import json
from chatgpt import *

app = Flask(__name__)
# app.secret_key = FLASK_SECRET_KEY

@app.route('/', methods=['GET'])
def test():
    return "Please use Post"

@app.route('/', methods=['POST'])
def send_msg():
    usermsg = request.get_json()
    print(usermsg)
    airesponse = callToOpenAI(usermsg['client'])
    print(airesponse)
    res = make_response(airesponse)
    res.mimetype = 'application/json'
    res.status_code = 200
    return res

@app.errorhandler(405)
def method_not_allowed(e):
    return 'Method not allowed', 405

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
from flask import Flask, request
import os, signal
from flask.json import jsonify


app = Flask(__name__)
# NEED TO Check How to use base_path in flask to set /v4 as base_path

@app.route('/')
def test():
    return 'Hello World'

@app.route('/v4/shorten',  methods=['POST'])
def shorten():
    content = request.get_json()    # If we are always expecting a json body we can use as it is else get_json(silent=True)
    print(content)
    return content


@app.route('/stopServer')
def stopServer():
    os.kill(os.getpid(),signal.SIGINT)
    return jsonify({"success": True, "message" :"Server is 	shutting down"})


if __name__ == "__main__":
    # app.run(debug=True)
    # 'for running on local'
    app.run(debug=False,host='localhost', port= 8070)
    # for running on https on local
    #context = ('ServerKeys/server.crt', 'ServerKeys/server.key')  # certificate and key files
    #app.run(debug=True, host='localhost', port= 8070, ssl_context=context)

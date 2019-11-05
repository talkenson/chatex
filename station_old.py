import os, sys, win32, time, json, random, time, datetime
from flask import Flask, request, Response, jsonify
from flask_cors import CORS
import _thread
from threading import Timer
import atexit
import uuid
import pickle


app = Flask(__name__)
CORS(app)
plugins = {}

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

history = []

tokens = {

}


letters = sum([
        [chr(s) for s in range(ord('a'), ord('z')+1)],
        [chr(s) for s in range(ord('A'), ord('Z')+1)],
        [chr(s) for s in range(ord('0'), ord('9')+1)],
        [
            '_','-','$','%','.']
        ], [])

motd = "Bad Guys"


def saveAll():
    with open('tokens.pickle', 'wb') as f:
        pickle.dump(tokens, f)
    with open('history.pickle', 'wb') as f:
        pickle.dump(history, f)

atexit.register(saveAll)

def loadAll():
    global tokens, history
    if os.path.exists('tokens.pickle'):
        with open('tokens.pickle', 'rb') as f:
            tokens = pickle.load(f)
    if os.path.exists('history.pickle'):
        with open('history.pickle', 'rb') as f:
            history = pickle.load(f)

loadAll()


@app.route('/reg/<string:uname>:<string:key>')
def reg(uname, key):
    return Response('{"status": "fail", "code": "0", "desc": "data isn\'t allowable"}', mimetype='application/json')

@app.route('/send', methods=['POST'])
def send():
    return Response('{"status": "fail", "code": "0", "desc": "data isn\'t allowable"}', mimetype='application/json')


@app.route('/updates', methods=['GET'])
@app.route('/send', methods=['GET'])
def err_usePost():
    return Response('{"status": "fail", "code": "500", "desc": "use POST request instead of GET"}', mimetype='application/json')

@app.route('/updates', methods=['POST'])
def updates():
    return Response('{"status": "fail", "code": "0", "desc": "data isn\'t allowable"}', mimetype='application/json')

@app.route('/messages')
def msglist():
    return Response('{"status": "fail", "code": "0", "desc": "data isn\'t allowable"}', mimetype='application/json')

@app.route('/tokens')
def toklist():
    return Response('{"status": "fail", "code": "0", "desc": "data isn\'t allowable"}', mimetype='application/json')


def gupd():
    global tokens, history
    while True:
        time.sleep(10)


if __name__ == '__main__':

    _thread.start_new_thread(gupd, ())
    app.run('0.0.0.0', port=12000, debug=False, threaded=True)

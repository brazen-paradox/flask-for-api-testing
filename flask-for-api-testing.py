#Author : Brazen Paradox
#File created on 30 May 2020 7:58 AM

from flask import Flask, request, json
import os

app = Flask(__name__)

@app.route('/apollo')
def apollo():
    return 'The Eagle has landed!'

@app.route('/')
def index():
    return 'Failure is not an option'

@app.route('/postme', methods=['post'])
def postme():
    data = request.data
    print(data)
    return str(data)


@app.route('/getme', methods=['get'])
def getme():
    # data = request.data
    # print(data)
    return bytes("got you", 'utf-8')

@app.route('/putme', methods=['put'])
def putme():
    data = request.data
    print(data)
    return data

@app.route('/deleteme', methods=['delete'])
def deleteme():
    data = request.data
    print(data)
    return data


if '__main__' == __name__:
    port = int(os.environ.get('PORT', 11000))
    app.run('0.0.0.0', port)



import os

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/calc')
def calc():
    arg1 = int(request.args.get('arg1'))
    arg2 = int(request.args.get('arg2'))
    return f'arg1+arg2={arg1+arg2}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

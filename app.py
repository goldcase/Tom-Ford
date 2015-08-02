#!flask/bin/python
# The above line is to specify which program to run this file with. We have virtualenv installed, so use that version of python.

from flask import Flask

app = Flask(__name__)

# TODO: Mock out some analytics requests.

@app.route('/tomford/api/v1.0/', methods=['GET'])
def index():
    return "Welcome to the Tom Ford rap analytics API!"

if __name__ == '__main__':
    app.run(debug=True)

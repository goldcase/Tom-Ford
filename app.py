#!flask/bin/python
# The above line is to specify which program to run this file with. We have virtualenv installed, so use that version of python.

from flask import Flask, jsonify

app = Flask(__name__)

# TODO: Mock out some analytics requests.

@app.route("/tomford/api", methods=["GET"])
def index():
    return jsonify({ "message": "Welcome to the Tom Ford rap analytics API!" })

@app.route("/tomford/api/syllables/", methods=["GET"])
def syllables():
	return jsonify({ "count": 3, "syllables": ["tom", "ford"] })

@app.route("/tomford/api/detect/", methods=["GET"])
def detection():
	return jsonify({ "message": "Detecting all schemes. Welcome." })

@app.route("/tomford/api/detect/perfect/", methods=["GET", "POST"])
def detect_perfect():
	return jsonify({ "message": "Detecting perfect rhymes." })

@app.route("/tomford/api/detect/multi/", methods=["GET", "POST"])
def detect_multis():
	return jsonify({ "message": "Detecting multis." })

if __name__ == '__main__':
    app.run(debug=True)

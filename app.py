#!flask/bin/python
# The above line is to specify which program to run this file with. We have virtualenv installed, so use that version of python.

from flask import Flask, jsonify, make_response, request
import nltk
import pprint
import string
from nltk.corpus import cmudict
from collections import defaultdict, OrderedDict

app = Flask(__name__)

transcr = cmudict.dict()

# TODO: Mock out some analytics requests.

# Normalizes the string, takes out any punctuation.
# Returns a list of words.
def normalize_and_split_string(s):
	# Deletes punctuation using string.translate tables, then lowers the case and splits it into a list.
	# Creates table mapping punctuation to None
	delete_punctuation_map = dict((ord(char), None) for char in string.punctuation)

	return s.translate(delete_punctuation_map).lower().split()

# Transcribes the string into tokens.
def transcribe_string(s):
	return [transcr[word][0] for word in normalize_and_split_string(s)]

def transcribe_list(l):
	return [transcribe_string(line) for line in l]

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({ "error": "Not found."}), 404)

@app.route("/tomford/api", methods=["GET"])
def index():
    return jsonify({ "message": "Welcome to the Tom Ford rap analytics API!" })

@app.route("/tomford/api/tokenize", methods=["POST"])
def tokenize():
	# Abort if there is no request or if the request doesn't contain the lyrics property.
	if not request.json or not "lyrics" in request.json:
		abort(400)
	lyrics = request.json["lyrics"]

	return jsonify({ "tokens": transcribe_list(lyrics) })

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

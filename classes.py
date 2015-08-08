# Python classes for Tom Ford.
class SyllableResult:
	"""
	Contains the result of calculating syllables for a single line.
	"""
	syllables = []
	count = 0

	def __init__(self, syllables, count):
		self.syllables = syllables
		self.count = count

class MessageResponse:
	message = ""

	def __init__(self, message):
		self.message = message

class TokenizedLyricsResponse:
	tokenized_lyrics = []

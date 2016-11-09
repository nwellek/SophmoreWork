import request
import json

def get_from_itunes (artist, media = "song"):
	d = {"term": artist, "entity": media}
	results = request.get("http://itunes.apple.com/search", params = d)
	python_results = results.json()
	return python_results
print get_from_itunes(artist = "Prince")


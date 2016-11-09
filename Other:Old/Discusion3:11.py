import request
import json

def get_from_itunes (artist, media = "song"):
	d = {"term": artist, "entity": media}
	results = results.get("http://itunes.apple.com/search?", params = d)


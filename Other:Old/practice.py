import requests
import json

def get_from_itunes (artist, media = "song"):
	d = {"term": artist, "entity": media}
	results = requests.get("http://itunes.apple.com/search", params = d)
	python_results = results.json()
	song_list = []
	for a in "results":
		for b in a:
			for x in b:
				if c == "trackName":
					song_list.append(b[c])
	return song_list



print get_from_itunes(artist = "prince")




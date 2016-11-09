#this week I learned how to draw stuff from the internet

import requests #first you have to import requests a module
import json #and most are in json format so import that as well
#
def get_from_itunes (artist, media = "song"):
	d = {"term": artist, "entity": media}
	results = requests.get("http://itunes.apple.com/search", params = d)
	python_results = results.json() #this will put all the data into a python format
	songs = python_results[""]
print get_from_itunes(artist = "drake")



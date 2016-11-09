def get_from_itunes(artist, media_type="song"): 
	list_of_items = [] 
	baseurl = "https://itunes.apple.com/search" 
	params_dict = {} # start an empty dictionary to hold the API request parameters
	params_dict["term"] = artist # the value of the term parameter, the thing to search for, should be the artist that you passed in to the function
	params_dict["entity"] = media_type # the value of the entity parameter should be the media_type, which will be either "song", "album", or "musicVideo"
	try: # the unsafe part is making a request to the internet and dealing with the results from it. THAT'S what would give you an error inside the function where you'd wanna jump to an except clause.
		response = requests.get(baseurl, params=params_dict) # use the requests library to get a response from the API with these parameters
		data = response.json() # use the .json() method on a response object to get the data into Python dictionary format
		if len(data["results"]) > 0: # If you want to be really careful, check to see if there were any responses, because earching for nonsense gives you an empty list of responses -- not an error.
			for item in data["results"]: # iterate over that list of results dictionaries we saw
				list_of_items.append(item["trackName"])
			return list_of_items
		else:
			print "Sorry, searching for {} did not work.".format(artist)
			return None
	except:
		print "Sorry, searching for {} did not work.".format(artist)
		return None

print get_from_itunes('prince')
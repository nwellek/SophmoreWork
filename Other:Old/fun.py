__author__ = 'Sam'
import requests


#Basic itunes item. Can represent most types of objects the itunes search API returns
class ItunesItem:
    def __init__(self,item_dict):
        self.kind = item_dict['kind']
        self.title = item_dict['trackName']
        self.release_date = item_dict['releaseDate']

    def get_description(self):
        return "Itunes item of type " + self.kind + " | Title: " + self.title + " | Release date: " + self.release_date

data_dict = {"kind":"song","trackName":"Lost Coastlines","releaseDate":"September 9, 2008"}






# Version of get_from_itunes you made last section
def get_from_itunes_2(term, entity="song"):
    try:
        r = requests.get('https://itunes.apple.com/search?limit=10', params={'term':term,'entity':entity})
        rdict = r.json()
        tracknames = []
        subdict_list = rdict['results']
        for subdict in subdict_list:
            tracknames.append(Song_v4(subdict['trackName'], subdict['artistName'], subdict['trackPrice'], subdict['trackTimeMillis']))
        return tracknames
    except:
        print 'Sorry, could not look up',entity,'for artist',term








#Version of get_from_itunes that creates ItunesItem instances, not Song_v4 instances
def get_from_itunes_3(term):
	for subdict in subdict_list:
		try:
			tracknames.append(ItunesItem(subdict))
		except:
			print "skipping"
    








# Represents a song returned by the itunes search API. Has everything a basic item has, plus a couple things
class ItunesSong(ItunesItem):
    def __init__(self,item_dict):
        ItunesItem.__init__(self,item_dict)
        self.artist = item_dict['artistName']
        self.album = item_dict['collectionName']

    def get_description(self):
        return "Itunes song | Title: " + self.title + " | Album: " + self.album + " | Artist: " + self.artist + " | Release date: " + self.release_date

data_dict2 = {"kind":"song","trackName":"Unless It's Kicks","releaseDate":"August 7, 2007", "collectionName":"The Stage Names", "artistName":"Okkervil River"}









# Represents a movie returned by the itunes search API. Has everything a basic item has, plus a couple things.
class ItunesMovie(ItunesItem):
    pass

data_dict3 = {"kind":"feature-movie","trackName":"O Brother, Where Art Thou?","releaseDate":"Feb 2, 2001", "contentAdvisoryRating":"pg-13", "artistName":"Coen Brothers"}









#Version of get_from_itunes that is capable of returning ItunesItems, ItunesSongs, and ItunesMovies, as appropriate
def get_from_itunes_4(term):
    pass
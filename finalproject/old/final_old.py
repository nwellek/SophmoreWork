import requests 
import json
import billboard




#################################__________________Spotify___________________________________#############################


baseurl_spotify = 'https://api.spotify.com/v1/users/'
spotify_secret = 'bc8d25d34bcc4b34ab7a8ec3867a6cb9'
spotify_id = 'cb53c896bdbe4fb8ae26ddda6245177a'
#new_key = raw_input("Enter the OAuth Token (https://developer.spotify.com/web-api/console/get-playlist/#complete)")
new_key = 'BQBnepnF28E7G0jtaCWvWgyhx8nU0n_sBU7LywfhcqI_TzPWuhk8Yu07rIhUpCCbEJN8mUgziQ8CPHZ9O8Cifvq6K8RYx__r1mrJODkYcHjafO5AlKcws0Mi0jkS7cW1kPQrYLcQwvFsEJE'


def get_playlist_Spotify(owner_id='spotify', playlist_id='4hOKQuZbraPDIfaGbM3lKI'):
    base_url = baseurl_spotify + owner_id + '/playlists/' + playlist_id
    authentication_key = new_key
    response = requests.get(base_url, headers={'Authorization':'Bearer ' + authentication_key})
    response = response.json()
    return response


def get_artistname_Spotify(response):
    artists = []
    for item in response['tracks']['items']:
        artists.append(item['track']['artists'][0]['name'])
    return artists
#__________________ uncomment below to see spotify top artist _________________________________
s = get_playlist_Spotify()
start = 0
print "These are the top 100 Spotify artists by song in order:"
for item in get_artistname_Spotify(s):
    item = item.encode('utf-8')
    start += 1
    print str(start)+ ". " + item.lower()


def get_top100songs_Spotify(response):
	songs = []
	for item in response['tracks']['items']:
		songs.append(item['track']['name'])
	return songs
#__________________ uncomment below to see spotify top songs _________________________________	
s = get_playlist_Spotify()
print "These are the top 100 Spotify songs in order:"
start = 0
for item in get_top100songs_Spotify(s):
	item = item.encode('utf-8')
	start += 1
	if "(" in item:
		print str(start)+ ". " + item.partition ("(")[0].lower()
	elif "-" in item:
		print str(start)+ ". " + item.partition ("-")[0].lower()
	else:
		print str(start)+ ". " + item.lower()
spotify_total = 0
for item in get_top100songs_Spotify(s):
	spotify_total +=1
if spotify_total == 100:
	print "Passed: You have a 100 Spotify songs"
else:
	print "Failed: You have " + str(spotify_total) + "Spotify songs"

print "************FINISHED WITH SPOTITY********************"


#################################__________________Billboard___________________________________#############################

chart = billboard.ChartData('hot-100')
#print chart
songs = []
for item in chart:
	songs.append(item.title)
#print songs
artist = []
for item in chart:
	artist.append(item.artist)
print artist
start = 0
print "These are the top 100 Billboard songs in order:"
for item in songs:
	start += 1
	print str(start)+ ". " + item.lower()
print "These are the top 100 Billboard artist in order:"
start = 0
for item in artist:
	start += 1
	if "Featuring" in item:
		print str(start)+ ". " + item.partition("Featuring")[0].lower()
	else:
		print str(start)+ ". " + item.lower()	
Billboard_total = 0
for item in chart:
	Billboard_total +=1
if Billboard_total == 100:
	print "Passed: You have a 100 Billboard songs"
else:
	print "Failed: You have " + str(Billboard_total) + "Billboard songs"
print "************FINISHED WITH BILLBOARD************"


#################################__________________iTunes___________________________________#############################
'''
username = 'nwellek'
Affiliate_ID = '1000ldB8'

def get_playlist_iTunes(artist, media_type="song"): 
	list_of_items = [] 
	baseurl = "https://itunes.apple.com/search/" #https://itunes.apple.com/us/rss/topsongs/limit=100/explicit=true/xml
	params_dict = {}							 
	params_dict["term"] = artist 
	params_dict["entity"] = media_type 
	return response


def get_artistname_iTunes(response):
    artists = []
    for item in response['tracks']['items']:
        artists.append(item['track']['artists'][0]['name'])
    return artists
#__________________ uncomment below to see iTunes top artist _________________________________
i = get_playlist_iTunes()
start = 0
print "These are the top 100 iTunes artists by song in order:"
for item in get_artistname_iTunes(i):
    item = item.encode('utf-8')
    start += 1
    print str(start)+ ". " + item


def get_top100songs_iTunes(response):
	songs = []
	for item in response['tracks']['items']:
		songs.append(item['track']['name'])
	return songs
#__________________ uncomment below to see iTunes top songs _________________________________	
i = get_playlist_iTunes()
print "These are the top 100 iTunes songs in order:"
start = 0
for item in get_top100songs_iTunes(i):
	item = item.encode('utf-8')
	start += 1
	if "(" in item:
		print str(start)+ ". " + item.partition ("(")[0]
	elif "-" in item:
		print str(start)+ ". " + item.partition ("-")[0]
	else:
		print str(start)+ ". " + item
iTunes_total = 0
for item in get_top100songs_iTunes(i):
	iTunes_total +=1
if iTunes_total == 100:
	print "Passed: You have a 100 iTunes songs"
else:
	print "Failed: You have " + str(iTunes_total) + "iTunes songs"
'''


#################################__________________Class___________________________________#############################



class Song():
	def __init__(self, song_title, song_artist):
		self.iTunes.ranking = 0
		self.spotify.ranking = 0
		self.downloads = 0
		self.plays = 0
		self.title = song_title
		self.artist = song_artist

	def get_avg_ranking(self):
		rank_both = self.iTunes.ranking + self.spotify.ranking
		rank_avg = rank_both/2
		return rank_avg

	def save_spotify_info(self, plays, ranking):
		self.plays = plays
		self.spotify.ranking = ranking

	def save_iTunes_info(self, downloads, ranking):
		self.downloads = downloads
		self.iTunes.ranking = ranking

	def get_metric(self):
		metric =  self.plays + self.downloads *100
		return metric

d = {}
def get_iTunes_info(d):
	for x in L:
		d[x] = d[x] + save_iTunes_info
	return d

def get_spotify_info(d):
	for x in L:
		if x in d:
			d[x] = d[x] + save_spotify_info
		else:
			d[x] = 1


#################################__________________CSV___________________________________#############################

#f = ("results.csv", "w")
#f.write = ("'Song', 'Metric Score', 'iTunes Rank', 'Spotify Rank', 'Average Rank'\n")
#for x in sorted_list:
#f.write ("self.title", "metric", "self.iTunes.ranking", "self.spotify.ranking", "rank_avg")




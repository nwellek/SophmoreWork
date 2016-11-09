import requests
import json
import billboard  # TODO: Write in your README need to install.
import test106 as test

class Song():
	def __init__(self, tup):
		self.name = tup[0]
		self.artist = tup[1]

		self.spotify_ranking = 0
		self.billboard_ranking = 0
		self.itunes_ranking = 0

	def get_avg_ranking(self):
		count = 0
		temp = 0
		if self.spotify_ranking != 0:
			count += 1
			temp += self.spotify_ranking

		if self.billboard_ranking != 0:
			count += 1
			temp += self.billboard_ranking

		if self.itunes_ranking != 0:
			count += 1
			temp += self.itunes_ranking

		if count == 0:
			print self.name, self.artist

		return float(temp) / count

	def __str__(self):
		s = self.name + "," + self.artist + ","
		if self.spotify_ranking == 0:
			s += '-'
		else:
			s += str(self.spotify_ranking)
		s += ','

		if self.billboard_ranking == 0:
			s += '-'
		else:
			s += str(self.billboard_ranking)
		s += ','

		if self.itunes_ranking == 0:
			s += '-'
		else:
			s += str(self.itunes_ranking)
		s += ','

		return s + self.get_avg_ranking() + "\n"

def clean_name(name):
	name = name.encode('utf-8')
	if "(" in name:
		return name.partition ("(")[0].lower()
	elif "-" in name:
		return name.partition ("-")[0].lower()
	else:
		return name.lower()

def spotify_source():
	baseurl_spotify = 'https://api.spotify.com/v1/users/'
	spotify_secret = 'bc8d25d34bcc4b34ab7a8ec3867a6cb9'
	spotify_id = 'cb53c896bdbe4fb8ae26ddda6245177a'

	oauth = "BQA6LM1BQIYhPU2K7zpqFCZLCX1ydPa29u0nukcBwjXvP0qA2zN35bWMdkiVy5j5WP5wrRG17fayIgnqbTaZcbBxl7y6xHgt-RJEW9uh4GlJEbIcQq02XI0tmlBMYyKNdmGOo8a69LQmI0E"
	if oauth == None:
		oauth = raw_input("Enter the OAuth Token (https://developer.spotify.com/web-api/console/get-playlist/#complete)")

	base_url = baseurl_spotify +'spotify/playlists/4hOKQuZbraPDIfaGbM3lKI'
	response = requests.get(base_url, headers={'Authorization':'Bearer ' + oauth})
	response = response.json()

	tup_list = [(clean_name(item['track']['name']), item['track']['artists'][0]['name']) for item in response['tracks']['items']]
	return tup_list

def billboard_source():
	chart = billboard.ChartData('hot-100')
	tup_list = [(clean_name(item.title), item.artist) for item in chart]
	return tup_list


def itunes_source():
	f =open("itunesdata.txt", 'r')
	x =json.load(f)

	tup_list = []
	for item in x['entry']:
		tup = (clean_name(item['name']), item['artist']['#text'].encode('utf-8'))
		tup_list.append(tup)
	return tup_list

songs = []

print "Retreiving Spotify data..."
spotify_songs = spotify_source()
print spotify_songs

for item in range(len(spotify_songs)):
	print item
	for song in spotify_songs:
		songs.append(Song(song).name)

# print songs

print "Retreiving Billboard data..."
billboard_songs = billboard_source()

print "Retreiving iTunes data..."
itunes_songs = itunes_source()

# songs[]
print songs
# sorted_list = sorted(songs, key=lambda x : songs[x].get_avg_ranking())
# for x in sorted_list:
# 	print type(x)

'''
	# Output
f = ("results.csv", "w")
f.write("Song, Artist, Spotify Rank, Billboard Rank, iTunes Rank, Average Rank\n")
for x in sorted_list:
	f.write(x.__str__())
f.close()
'''

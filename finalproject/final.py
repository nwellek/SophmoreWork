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
			return "sorry"

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
	name = name.rstrip()
	name = name.encode('utf-8')
	if " -" in name: 
		return name.partition (" -")[0].lower()
	if "," in name:
		if "(" in name:
			return name.replace(",", "").partition(" (")[0].lower()
		elif "-" in name: 
			return name.replace(",", "").partition("-")[0].lower()
		else:
			return name.replace(",", "").lower()
	if " (" in name:
		if "," in name:
			return name.replace(",", "").partition(" (")[0].lower()
		else:
			return name.partition (" (")[0].lower()
	if "(" in name:
		return name.partition ("(")[0].lower()
	if "-" in name: 
		return name.partition ("-")[0].lower()
	if " -" in name: 
		return name.partition (" -")[0].lower()
	else:
		return name.lower()

test.testEqual(clean_name('me, myself'), 'me myself')
test.testEqual(clean_name('me, myself-fear'), 'me myself')
test.testEqual(clean_name('me, myself (feat'), 'me myself')
test.testEqual(clean_name('one dance ('), 'one dance')
test.testEqual(clean_name('one dance '), 'one dance')
test.testEqual(clean_name('one dance- feat drake '), 'one dance', "Clean Name")

oauth = raw_input("Enter the OAuth Token. To get ouath goto (https://developer.spotify.com/web-api/console/get-playlist/#complete) (owner id = spotify) (playlists id =4hOKQuZbraPDIfaGbM3lKI)")
#oauth = "BQBKBq2WKabFgZwFk5IQa1HVLnC3rwuDBjGh3bhKaUDNITzYOPbfL2xjho4Ff3QbpKwHF48CJfVLqZjGoNhZpR0Z718a838WfByMiNZtDCwslD1d6W_seEiqpNyVSaVBHj_qlyrG2oGE5Hk"

def spotify_source():
	baseurl_spotify = 'https://api.spotify.com/v1/users/'
	spotify_secret = 'bc8d25d34bcc4b34ab7a8ec3867a6cb9'
	spotify_id = 'cb53c896bdbe4fb8ae26ddda6245177a'
	owner_id = "spotify"
	playlists_id = "4hOKQuZbraPDIfaGbM3lKI"
	base_url = baseurl_spotify +'spotify/playlists/4hOKQuZbraPDIfaGbM3lKI'
	response = requests.get(base_url, headers={'Authorization':'Bearer ' + oauth})
	response = response.json()

	tup_list = [(clean_name(item['track']['name']), clean_name(item['track']['artists'][0]['name'])) for item in response['tracks']['items']]
	return tup_list
test.testEqual(len(spotify_source()), 100, "Spotify test")

def billboard_source():
	chart = billboard.ChartData('hot-100')
	tup_list = [(clean_name(item.title), clean_name(item.artist)) for item in chart]
	return tup_list

test.testEqual(len(billboard_source()), 100, "Billboard test")
def itunes_source():
	f =open("itunesdata.txt", 'r')
	x =json.load(f)

	tup_list = []
	for item in x['entry']:
		tup = (clean_name(item['name']), clean_name(item['artist']['#text']))
		tup_list.append(tup)	
	return tup_list
test.testEqual(len(itunes_source()), 100, "iTunes test")
if __name__ == "__main__":
	songs = {}

	print "Sourcing from Spotify..."
	spotify_songs = spotify_source()

	print "Sourcing from Billboard..."
	billboard_songs = billboard_source()

	print "Sourcing from iTunes..."
	itunes_songs = itunes_source()

	for s in enumerate(spotify_songs):
		songs[s[1][0]] = Song(s[1])
		songs[s[1][0]].spotify_ranking = s[0] + 1


	for s in enumerate(billboard_songs):
		if s[1][0] not in songs:
			songs[s[1][0]] = Song(s[1])
		
		songs[s[1][0]].billboard_ranking = s[0] + 1

	for s in enumerate(itunes_songs):
		if s[1][0] not in songs:
			songs[s[1][0]] = Song(s[1])		

		songs[s[1][0]].itunes_ranking = s[0] + 1

	sorted_list = sorted(songs, key=lambda x : songs[x].get_avg_ranking())


	# Output
	f = open("results.csv", "w")
	f.write("Song, Artist, Spotify Rank, Billboard Rank, iTunes Rank, Average Rank\n")
	for x in sorted_list:
		f.write(("{}, {}, {}, {}, {}, {}\n".format(songs[x].name, songs[x].artist, songs[x].spotify_ranking, songs[x].billboard_ranking, songs[x].itunes_ranking, songs[x].get_avg_ranking())))
	f.close()


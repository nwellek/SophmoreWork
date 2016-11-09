import requests
import json
import test106 as test
## PROBLEM SET 12

## [PROBLEM 1]

# Below is a function called blanked_word, very similar to one you've seen before. DO NOT change the function! 

def blanked_word(secret_word, guesses):
    final_string = ""
    for ch in secret_word.upper():
        if ch in guesses.upper():
            final_string = final_string + ch
        else:
            final_string = final_string + "_"
    return final_string

# The function should accept 2 strings as input: a secret word for the player to guess in a Hangman game, and a collection of the letters that have already been guessed by the player. It should return a string with the letters of the word in the right places if they have been guessed, all in uppercase. If a letter has not been guessed, there should be a _ (an underscore) in that place. 

# Write at least three non-trivial return-value tests to determine whether it works correctly, here:
test.testEqual(blanked_word('catsarecool','acs'),'CA_SA__C___')
test.testEqual(blanked_word('dog','o'),'_O_')
test.testEqual(blanked_word('nate','at'),'_AT_')


## [PROBLEM 2]

# Write at least 3 return value tests and at least 4 side-effect tests for this class definition.
# At least one of your tests should apply to each method of the class.
class Song:
    def __init__(self,artist,title,album="Burned Mix"):
        self.artist = artist
        self.title = title
        self.album = album
        self.number_plays = 0

    def play(self, repeats=1):
        self.number_plays = self.number_plays + repeats

    def num_words_title(self):
        return len(self.title.split())

    def __str__(self):
        return "Song Title: {}\nArtist: {}\nOn :{}\nPlayed {} times.".format(self.title,self.artist,self.album,self.number_plays)

x = Song(artist='Drake', title='Good')
# Write your return value tests below this line:
y= x.play(repeats=5)
test.testEqual(x.number_plays, 5)
z = x.play(repeats=2)
test.testEqual(x.number_plays, 7)
test.testEqual(x.num_words_title(), 1) 
test.testEqual(x.__str__(), "Song Title: Good\nArtist: Drake\nOn :Burned Mix\nPlayed 7 times.") 

# Write your side-effect tests below this line:

test.testEqual(x.artist, 'Drake')
test.testEqual(x.title, 'Good')
test.testEqual(x.album, 'Burned Mix')
y = x = Song(artist='Drake', title='Good', album="Burned Mix2")
test.testEqual(x.album, 'Burned Mix2')
# Make sure you've put your tests in the right place under the comments -- we need to see that you understand the difference between return value tests and side-effect tests!




## [PROBLEM 3]

# This last problem is some nested data and API request practice. 

# You will need to:
# - use an API we have not used yet for a problem set, get back nested JSON-formatted data, cache some data that you get back, and parse the cached data so you get clear, readable results that we can see (and code that we can run!).
# - the data you ultimately extract must be at least 2 levels deep in the nested data you get back, and you must iterate over some sequence in the data in order to get your printed result.
# - print out, for us, what data you've decided to access and what API you've decided to use!
# Fill in your code in the several "Parts" below, not right here...


# For example: If we had not used Flickr yet in the class, you might use the Flickr API, make a search for photos by a tag, and print out the title of each photo and the username of the person who posted it.
# It would not be acceptable to print out only one photo title, or only one photo's tags, because that wouldn't involve any iteration.

# You should not print out dictionaries -- find some part of the data that is easily human-readable, figure out what it means ("this represents the title of the photo" or "this represents the text in a comment" for example), and write code to access and print it.

# Since we _have_ used Flickr, you must choose some new-to-you data, and make your own decisions about what data you will get from it! 

# Note that you MAY use the data you get back and any code you write in this problem for your final project (at least, it may be a good starting point!).

# If you wish to do something more complicated than printing stuff out (accumulating frequencies of something in a dictionary, for example, and printing the key-value pairs in that dictionary), that is totally OK (that could help you get further on your final project!), but it is not required for this problem set.

# Some APIs students have used in previous semesters:
# New York Times: http://developer.nytimes.com/docs/read/article_search_api_v2
# Tumblr (a lot like Twitter): https://www.tumblr.com/docs/en/api/v2
# Reddit: https://www.reddit.com/dev/api
# OMDB: http://www.omdbapi.com/

# Feel free to find your own (and to share it on the Facebook group)! Make sure any API you choose has good documentation, and that you can get JSON data from it.


## [PART 1]
## Write a print statement that will print out a string with the API you use and what data you are going to get. For example, print out
## "I am using the Flickr API and will print out the title and author name for each photo, from a series of photos that comes from searching for a tag."

## Write that print statement here:
print " I am using the Spotify API and will print out artists name for a given playlist, that I will search by the playlist tag"

## [PART 2]
## Make a request, cache data from the request, and parse that data.
## Include your cached data file with your submission so we can run your code!

## The approximate steps you should take to complete this are as follows:

# 1. Choose a REST API and read its documentation. (Note that many APIs, like Flickr, and Twitter, have a bunch of different endpoints that require different parameters and get you different results, and required query parameters will vary.) 

# Get an idea for what the data should look like when you make a good request, perhaps by going to an example URL in the browser. (I suggest filling out the chart you can find here, for your API: https://umich.instructure.com/courses/48961/files/folder/Final%20Project?preview=1410462)

# 2. Try making a request or two. Make sure it's working properly, that you have the right query parameters and the right path, that you're using authentication correctly if it needs it, etc.

# 3. Make a request and cache resulting data in a file.

# 4. Write some code to get the cached JSON-formatted data into a Python object you can use in your program. (See the textbook, and PSets 9 and 10, for hints if you've forgotten how to do this.)

# 5. Do some investigation into the nested data to figure out what's there, and what you want to extract. Paste it into jsoneditoronline.org, maybe. Write some print statements: what type is the object you get back? what are the keys, if it's a dictionary? If you get to a list, what are the elements of a list? What type is each element? and so on.

# 6. Finally, write code to iterate over the proper parts of the data and extract the inner pieces of it that you want.

# 7. Run your code, using your cached data, to print out pieces of data in a clear way. Success! Be sure to upload your cached data file as well as your code file when turning in the problem set.
baseurl_spotify = 'https://api.spotify.com/v1/users/'
spotify_secret = 'bc8d25d34bcc4b34ab7a8ec3867a6cb9'
spotify_id = 'cb53c896bdbe4fb8ae26ddda6245177a'
#new_key = raw_input("Enter the OAuth Token (https://developer.spotify.com/web-api/console/get-playlist/#complete)")
my_OAuth = 'BQCPfGa9J8oh9HidUe6AELwSNDO-ael2MLkxAOiZMBMJCoI4hPbtgksbc6Q-YxFELiYg5qEMGtuRLZSvcFHyqffYZ8YCF64B-_qFYDkKIQn9ZnQi0kljMc1uSV4lSnpBLU8dj-9yFm82RSQ'
new_key = my_OAuth

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

x = get_playlist_Spotify()
start = 0
print "These are the top 100 Spotify artists by song in order:"
for item in get_artistname_Spotify(x):
    item = item.encode('utf-8')
    start += 1
    print str(start)+ ". " + item


f = open('nested.txt', 'w')
f.write(json.dumps(x))
f.close()


x = open('nested.txt', 'r') 

def get_artistname_Spotify_fromtxt(response):
    artists = []
    open('nested.txt', 'r') 
    for item in response['tracks']['items']:
        artists.append(item['track']['artists'][0]['name'])
    return artists
z = get_artistname_Spotify_fromtxt(x)
start = 0
print "These are the top 100 Spotify artists by song in order:"
for item in get_artistname_Spotify_fromtxt():
    item = item.encode('utf-8')
    start += 1
    print str(start)+ ". " + item

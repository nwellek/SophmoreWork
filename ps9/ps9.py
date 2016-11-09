# import statements
import test106 as test
import json
import requests

print "My name is Nate Wellek"
## PART 1 - MECHANICS (of user-defined classes)

# [PROBLEM 1]

## We'll go through the process of defining a class to describe a photograph on Flickr.
## We've provided some of the information filled in for this first example.
## Then you'll complete the same structure on your own for a different type of thing.

# The following exercises are a thought exercise to help you think about how you would
# define a class to represent a flickr photo.

# The name of your class will be... 
new_class_name = "Photo"

# An instance of the class will represent one
represents = "photograph on flickr"

# The Photo class should have how many instance variables?
# Let's say you want each Photo to have: a title, an author, and a list of tags.
num_instance_vars = 3 # when you decide this, 
					  # you have to think about what attributes you want to keep track of!

# One method of your class, other than __init__, will be named:
one_class_method = "display_info"

# When invoked, that method will...
method_description = "display all the info about the photo for the user, like the title, author, tags"
also = "There may also be other methods of this class"

total_string = """
The name of my class will be {}. One instance of the class will represent one
{}. The class will have {} instance variables. One method of my class, other 
than __init__, will be named {}. When invoked, that method will 
{}. {}.
""".format(new_class_name, represents, num_instance_vars, one_class_method, method_description, also)
# this line will print out the above paragraph with the information provided above filled in.
print total_string

### Now, do this again by yourself for a car. If you were to define a class to represent a car object, what might you pick for instance variables and methods? Fill in the blank strings/integers as directed below. Then run the program, so you can see a full paragraph about the class you've planned out.

# The name of your class will be... 
car_class_name = "car" 
# An instance of the class will represent one
reps = "one car"
# The class should have how many instance variables?
num_inst_vars = 3
# Fill in these variables with what some instance variables could represent below -- at least three.
inst_var_1 = "Brand of car"
inst_var_2 = "Model of car"
inst_var_3 = "Year the car was manufactured"

# One method of your class, other than __init__, will be named...
# Think: anything you want a car to do. 
#  Change license registration and print something out? Drive forward? 
car_class_method = "drive"

# When invoked, that method will...
# (Think: How would you represent this method you named above in code or in text 
# for someone to see in a program? 
# Look at the examples given in the textbook and the flickr Photo class above.) 
car_method_description = "this moves the car forward"

car_str = """The name of this class will be: {}. So you are creating a type {}.
An instance of the class will represent one {}. It should have {} instance
variables, which could represent: {},{},{}... One method of this class will be called {}, which 
will {}.
""".format(car_class_name,car_class_name,reps,num_inst_vars, inst_var_1,inst_var_2,inst_var_3,car_class_method, car_method_description)
print car_str


# [PROBLEM 2]

# Here is a class definition to represent a photo object. Of course, this is not the only way to design a photo class -- but it is a possibility! Take a look at the code and make sure you understand it.

class Photo():
	def __init__(self, title, author, tags):
		self.title = title
		self.author = author
		self.tags = tags

	def display_info(self):
		retval = "Photo: "
		retval += self.title + "\n"
		retval += "Photographed by: " + self.author + "\n"
		retval += "Tags: "
		for tag in self.tags:
			retval += tag + " "
		return retval

## Write one line of code to create an instance of the photo class and store the instance in a variable my_photo. 
my_photo = Photo("Photo1", "Ansel Adams", ["Nature", 'Mist', 'Mountain'])
## After you do that, my_photo.display_info() should produce the same string as the one stored in display_string.

# HINT: if you just call the constructor for the Photo class appropriately, everything will be taken care of for you. You just have to figure out, from the definition of the class, what to pass to the constructor. Remember the examples of creating a class instance from the textbook and from lecture/section!



# DO NOT CHANGE THE STRING STORED IN THIS VARIABLE - it is just for comparison!
display_string = "Photo: Photo1\nPhotographed by: Ansel Adams\nTags: Nature Mist Mountain "

try:
	test.testEqual(my_photo.display_info(), display_string, "Problem 2")
except:
	print "Failed Test for problem 2; my_photo variable not assigned or code for display_info or display_string was changed..."



### PART 2: Get data from Flickr - useful stuff for the rest of the Problem Set

flickr_key = "9597eca0bd45c542bae45789c765b0a0" # paste your flickr key here, so the variable flickr_key contains a string (your flickr key!)
if not flickr_key:
    flickr_key = raw_input("Enter your flickr API key, or paste it in the .py file to avoid this prompt in the future: \n>>")

## Useful function definition provided for you below.
## (You've seen this before, in the textbook. Other functions provided for you in the textbook may be useful in this Problem Set, too, if you understand how to use them...)

def flickrREST(baseurl = 'https://api.flickr.com/services/rest/',
    method = 'flickr.photos.search',
    api_key = flickr_key,
    format = 'json',
    cache_fname="cached_data.txt",
    extra_params={}):
    d = {}
    d['method'] = method
    d['api_key'] = api_key
    d['format'] = format
    for k in extra_params:
        d[k] = extra_params[k]
    resp = requests.get(baseurl, params = d)
    # print resp.url
    # cache the contents in a file
    print "caching data"
    f = open(cache_fname, 'w')
    f.write(resp.text)
    f.close()
    # return the contents as text in this case
    return resp.text


# [PROBLEM 3]

# Get a response from flickr: data for 50 photos that are tagged with 'sunset'.
# Save the text of the response in a file called flickr_response.txt (caching the data!).
flickrREST(cache_fname="flickr_response.txt", extra_params = {'tags': 'sunset', 'per_page' : 50})




# [PROBLEM 4] Making a tag recommender, using the Flickr API!

# In this problem, we'll walk you through steps you need to take to make a tag recommender, but we won't be providing you any code. You'll use the documentation we've copied in here, the code you've seen in lecture and section, and the functions provided above, to translate the English into Python and make your program work.

# Go through step by step. You may want to look back at other problem sets and Hackpad exercises to remind you of how to deal with nested data and with cached data from a REST API response.

# We've included a file called flickr_data.txt that you should have saved in the same directory as this file. That contains data from Flickr, the results of a tag search. It's data about 50 photos on Flickr that have the tag 'mountains.'

# Let's start making the tag recommender! This has several steps, which we'll walk you through in comments. 


## (1) Extract the contents of the cached data file flickr_data.txt we provided (use the one we provided, so we can test it!) into a Python dictionary. Save the dictionary in the variable flickr_diction.
a = open("flickr_data.txt", "r")
b = a.read()
flickr_diction = json.loads(b[14:-1])

# For testing your data extraction. Uncomment the following to run the test.
#test.testEqual(flickr_diction,json.loads(open("flickr_data.txt").read()))


## (2) Extract each of the photo ids from that response, making a list of all of them. Save the list in the variable photo_ids_list.
photo_ids_list = []
for x in flickr_diction['photos']['photo']:
    photo_ids_list.append(x['id'])
print photo_ids_list



## (3) For each of the photo ids, make a request to the flickr API method flickr.photos.getInfo (this is like the flickr.photos.search in flickrREST) -- it describes the place to go to get the data within the flickr service. See documentation at https://www.flickr.com/services/api/flickr.photos.getInfo.html.
for z in photo_ids_list:
    s = flickrREST(extra_params={'photo_id' : z}, method='flickr.photos.getInfo')
    n = s[14:-1]
    s = json.loads(n)

## (4) Extract the tags used on each photo, and accumulate frequencies with which each tag occurs across all those photos you found when you searched. In other words, you started out with data about 50 different photos. How many times does the tag 'nature' occur across all of those photos? What about the tag 'river'? Etc. All of those frequencies should be accumulated.
new_dictionary = {}
for each_id in photo_ids_list:
    if each_id not in new_dictionary:
        new_dictionary[each_id] = 1
    else:
        new_dictionary[each_id] = new_dictionary[each_id] + 1
print new_dictionary


## (5)  Sort a list of all those tags, based on how often they were used in the 50 photos.
sorted_list = sorted(new_dictionary.keys(), key = lambda x: new_dictionary[x], reverse = True)


## (6) Output (print, for the user to see) the five tags (other than the searched on tag) that were used MOST frequently!

## HINT 1: Take a slice of the sorted list.
## HINT 2: Skip the first element in the sorted list. That will be "mountains", since all the photos have that tag.
## (If you made this a live tag recommender, instead of using the data we gave you, you could have a user type in a tag to search for and get recommendations for Flickr tag searches that will get you similar photos.)

print "Below this line, the 5 most frequently used tags should print out:\n"
print sorted_list[1:6]

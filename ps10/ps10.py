###################
import json
import random
import requests
import test106 as test


#### PART 1: Class Inheritance mechanics

# [PROBLEM 1]

# We've provided a definition of a class Student, similar to the one you may have seen in lecture. Do not change this code:

class Student():
    def __init__(this_Student,name,years_at_umich=1):
        this_Student.name = name
        this_Student.years_UM = years_at_umich
        this_Student.bonus_points = random.randrange(1000)

    def shout(this_Student,phrase_to_shout):
        print phrase_to_shout # print is for ppl!
        
    def __str__(this_Student):
        return "My name is {}, and I've been at UMich for about {} years.".format(this_Student.name,this_Student.years_UM)

    def year_at_umich(this_Student):
        return this_Student.years_UM
##### DONE WITH STUDENT CLASS DEFINITION


# Define a subclass of Student, Programming_Student. 
# - The Programming_Student class should have an instance variable called number_programs_written, whose initial value is 0. 
# - The Programming_Student class should also have an instance method called write_programs. The write_programs method accepts an optional parameter called progs, which should be an integer representing the number of programs the Programming_Student will write. Its default value is 1. When the write_programs method is called on an instance of Programming_Student, the progs number is added to the instance's number_programs_written.
# - The printed representation of an instance of Programming_Student should look something like "My name is Jackie, I've been at UMich for about 100 years, and I have written 9 programs while here."
# - When the shout method is called for the Programming_Student class, the phrase "Also, Python is pretty cool." should print after the phrase to shout. You should be calling the parent shout method to make this happen.

# Write your code here.
class Programming_Student(Student):
    def __init__(this_Student, name, years_at_umich = 1):
        Student.__init__(this_Student, name, years_at_umich)
        this_Student.number_programs_written = 0
    def write_programs(this_Student, progs = 1):
        this_Student.number_programs_written += progs
    def __str__(this_Student):
        return "My name is {}, I've been at UMich for about {} years, and I have written {} programs while here.".format(this_Student.name, this_Student.years_UM, this_Student.number_programs_written)
# The following code should work if you have successfully defined Programming_Student as specified! Do not change this code, but feel free to make other print statements outside of it if that helps you!
print "==========="
pst = Programming_Student("Jess",3)
test.testEqual(pst.number_programs_written,0)
pst.write_programs()
test.testEqual(pst.number_programs_written, 1)
pst.write_programs(4)
test.testEqual(pst.number_programs_written,5)
print pst # should print: My name is Jess, I've been at UMich for about 3 years, and I have written 5 programs while here.
test.testEqual(pst.__str__(),"My name is Jess, I've been at UMich for about 3 years, and I have written 5 programs while here.")
pst.shout("I'm doing awesome on this problem set.") # Should print: I'm doing awesome on this problem set.
# Also, Python is pretty cool.
print "==========="



#### PART 2: Facebook API problem solving

# Provided for your use 
def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

# This code makes lists of positive words and negative words, saving them in the variables pos_ws and neg_ws. DO NOT CHANGE THIS CODE, you'll need it later in the PSet.
pos_ws = []
f = open('positive-words.txt', 'r')

for l in f.readlines()[35:]:
    pos_ws.append(unicode(l.strip()))
f.close()

neg_ws = []
f = open('negative-words.txt', 'r')
for l in f.readlines()[35:]:
    neg_ws.append(unicode(l.strip()))

### Now begin more graded problems.

# [PROBLEM 3] 
    # Fill in the definition of the class Post to hold information about one post that you've made on Facebook.
    # Add to the __init__ method additional code to set the instance variables comments and likes. 
    # More instructions about that follow, in the code below.
    # You need to pull out the appropriate data from the json representation of a single post. 
    # You can find a sample in the file samplepost.txt. 
    # There are tests that check whether you've pulled out the right data.
    
class Post():
    """object representing status update"""
    def __init__(self, post_dict={}):
        if 'comments' in post_dict:
            self.comments = post_dict['comments']['data']
        else: self.comments = []

        if 'likes' in post_dict:
            self.likes = post_dict['likes']['data']
        else: self.likes = []

      
        if 'message' in post_dict:
            self.message = post_dict['message']
        else:
            self.message = ""

        # [PROBLEM 3A] if the post dictionary has a 'comments' key, set an instance variable self.comments
        # to the list of comment dictionaries you extract from post_dict. Otherwise, set self.comments to be an empty list: []

        # Something similar has already been done for the contents (message) of the original post, which is the value of the 'message' key in the dictionary, when it is present (photo posts don't have a message). See above.

        # Extracting the list of comment dictionaries from a post_dict is a little harder. Take a look at the sample of what a post_dict looks like in the file samplepost.txt to figure out where to find the right information.
        
        # [PROBLEM 3B] Now, similarly, if the post has any likes, set self.likes to the value of the list of likes dictionaries. Otherwise, if there are no 'likes', set self.likes to an empty list.


    # [PROBLEM 4] In the Post class, fill in three methods:
    # -- positive() returns the number of words in the message that are in the list of positive words called pos_ws (provided in our code)
    # -- negative() returns the number of words in the message that are in the list of negative words called neg_ws (provided in our code)
    # -- emo_score returns an integer: the difference between positive and negative scores
    # The beginnings of these functions are below -- fill in the rest of the method code! There are tests of these methods later on.
        
    def positive(self):
        tot_pos = 0
        for words in self.message.split():
            if words in pos_ws:
                tot_pos += 1
        return tot_pos
                   
    def negative(self):
        tot_neg = 0
        for words in self.message.split():
            if words in neg_ws:
                tot_neg +=1
        return tot_neg

    def emo_score(self):
        return self.positive() - self.negative()        

# [PROBLEM 5] Add comments for these lines of code explaining what is happening in them.
sample = open('samplepost.txt').read() #The variable sample is assigned to a string of the text of samplepost.txt.
sample_post_dict = json.loads(sample) #The variable sample_post_dict is taking the string sample and turning it into a python object. 
p = Post(sample_post_dict) #The variable p is being assigned as sample_post_dic as an objet of the Post class.

# Use the next lines of code if you're having trouble getting the tests to pass. They will help you understand what a post_dict contains, and what your code has actually extracted from it and assigned to the comments and likes instance variables.
#print pretty(sample_post_dict)
#print pretty(p.comments)
#print pretty(p.likes)

# Here are tests for instance variables set in your __init__ method
print "-----tests for instance variables in class Post"
try:
    test.testEqual(type(p.comments), type([]), "testing type of p.comments")
    test.testEqual(len(p.comments), 4, "testing length of p.comments")
    test.testEqual(type(p.comments[0]), type({}), "testing type of p.comments[0]")
    test.testEqual(type(p.likes), type([]), "testing type of p.likes")
    test.testEqual(len(p.likes), 4, "testing length of p.likes")
    test.testEqual(type(p.likes[0]), type({}), "testing type of p.likes[0]")
except:
    print "One or more of the test invocations is causing an error. Cause for further examination: do some debugging!"

# Here are some tests of the positive, negative, and emo_score methods.
print "-----tests for methods in class Post"
p.message = "adaptive acumen abuses acerbic aches for everyone" # this line is to use for the tests, do not change it
test.testEqual(p.positive(), 2, "testing return value of .positive()")
test.testEqual(p.negative(), 3, "testing return value of .negative()")
test.testEqual(p.emo_score(), -1, "testing return value of .emo_score()")        
    
# Now, get a json-formatted version of your last 100 posts on Facebook. 
# (Hint: use https://developers.facebook.com/tools/explorer to get your access token, and fill in the query parameters dictionary with the access_token and the correct fields, as discussed in the textbook.
# Every couple hours you will need to get a new token.
# This is almost the same as the Facebook code example you saw in class.)

# Fill in your access token (in quotes, because it's a string) in the code if you don't want to have to paste it every time you run the program (but you'll have to replace it every couple hours).
access_token = "CAACEdEose0cBAL8GbREFeUue24PTsGyP3quZBIbGzlieag7ZBWA2ZCv1ZAqu7wxITgogZCUDO90HkI1mqM0ABCmHBZBQxe0BG5LZAhu9ZBLtNoYz3cCKOiANhSWLhIwK08kZBZB6kA5IvWi5nGJdADJxtJBRHEHV99J5zpIY3ZAIvbzV4bSZA5Qeu4RdHzwluawG2l2dAA8ZAa4XCZAhRYDBAdkB8VrXVVjJWlfehrSjDOZBZB8BaEetdtUkcXp5"
if access_token == None:
    access_token = raw_input("\nCopy and paste token from https://developers.facebook.com/tools/explorer\n>  ")

baseurl = "https://graph.facebook.com/v2.3/me/feed"
## If you do not have a Facebook account with any feed posts,
## you can use our group: replace the "me" in the baseurl with this id string: "1752935254934382" (our facebook group ID)
url_params = {}
url_params["access_token"] = access_token
# Write code to fill in other url_parameters dictionary here.
url_params['limit'] = 100
url_params['fields'] = 'message,comments,likes' 


# then uncomment the following line, which makes a request to the Facebook API as you're familiar with
feed = requests.get(baseurl,params=url_params)
d = json.loads(feed.text)
print pretty(d)
print '------------'



## Note that you will need to get the user_groups permission with your access token to do this, as discussed in class on Wednesday.

# [PROBLEM 6]
# # Use a list comprehension to create the list of post instances:
# For each of those posts in the feed you get back,
    # -- create an instance of your class Post.
    # Save all the post instances in a list called post_insts.
    # If you passed the tests above, all this should work just fine if you create one instance per post and save them all in a list, using a list comprehension structure.
    # This requires understanding -- but not very many lines of code!
    

# Write code to do that here:
post_insts = [Post(post_dict) for post_dict in d['data']]

try:
    print "testing whether the list post_insts exists and is the right kind of thing"
    test.testEqual(type(post_insts), type([]), "testing for list type")
    test.testEqual(len(post_insts) > 0, True, "testing whether there are multiple posts in the list")
    test.testEqual(type(post_insts[0]),type(Post({})), "testing whether the list has post instances")
except:
    print "failed tests for problem 6 or there is another error"


try:
    print "testing whether the list post_insts exists and is the right kind of thing"
    test.testEqual(type(post_insts), type([]), "testing for list type")
    test.testEqual(len(post_insts) > 0, True, "testing whether there are multiple posts in the list")
    test.testEqual(type(post_insts[0]),type(Post({})), "testing whether the list has post instances")
except:
    print "failed tests for problem 6 or there is another error"


# [PROBLEM 7] 
# Write code to compute the top 3 likers and the top 3 commenters on your posts overall, and save them in lists called top_likers and top_commenters. So top_likers should contain 3 names of people who made the most likes on all your Facebook posts, and top_commenters should contain 3 names of people who made the most comments on all your Facebook posts.
# HINT: creating dictionaries and sorting may both be useful here!

all_top_likers = {}
for x in d['data']:
    if 'likes' in x:
        for each in x['likes']['data']:
            eachname = each['name']
            if eachname not in all_top_likers:
                all_top_likers[eachname] = 0
            all_top_likers[eachname] = all_top_likers[eachname] + 1


likers = sorted(all_top_likers.keys(), key=lambda k: all_top_likers[k], reverse = True)

top_likers = likers[:3]

all_Com = {}
for y in d['data']:
    if "comments" in y:
        for e in y['comments']['data']:
            eachcomm = e['from']['name']
            if eachcomm not in all_Com:
                all_Com[eachcomm] = 0
            all_Com[eachcomm] = all_Com[eachcomm] + 1

commenters = sorted(all_Com.keys(), key=lambda c: all_Com[c], reverse = True)

top_commenters = commenters[:3]


 
### Code to help test whether problem 7 is working correctly
try: 
    print "Top commenters:"
    print top_commenters
    for p in range(len(top_commenters)):
        print p, top_commenters[p]

    print "Top likers:"
    print top_likers
    for p in range(len(top_likers)):
        print p, top_likers[p]
except:
    print "Problem 7 not correct.\ntop_commenters and/or top_likers has not been defined or is not the correct type, or you have another error."

# [PROBLEM 8] 
# Write code to find out: were there more unique commenters or more unique likers? 
# In other words: Is the number of unique people who commented in your feed, or the number of unique people who liked posts in your feed, larger? (Each person should only get counted once among commenters, and once among likers.)
# (Note that this is NOT the same as looking at whether there were more comments or likes!)
# If there were more unique commenters, write code to print "There were more unique commenters: <number of unique commenters>"
# If there were more unique likers, write code to print "There were more unique likers: <number of unique likers>" (replace the <number> with the actual number). If there are an equal number, the code should print "There are an equal numbers of unique commenters and likers."

# Write your code here.
unique_like = len(all_top_likers)

unique_comm = len(all_Com)

if unique_like > unique_comm:
    print "There were more unique likers: {}".format(unique_like)
elif unique_like < unique_comm:
    print "There were more unique commenters: {}".format(unique_comm)
else:
    print "There are an equal numbers of unique commenters and likers."


  
# [PROBLEM 9] 
# Write code to output a .csv file called emo_scores.csv that lets you make scatterplots (in Excel or Google sheets) showing net positivity (emo_scores) on x-axis and comment-counts and like-counts on the y-axis. 
# Each row should represent one post, and should include: emo score, comment counts, and like counts, in that order.
emo = []
for posts in post_insts:
    emo.append(posts.emo_score())

comments_9 = []
for c in d['data']:
    if 'comments' in c:
        x = len(c['comments']['data'])
        comments_9.append(x)
    else:
        x = 0
        comments_9.append(x)



likes_9 = []
for l in d['data']:
    if 'likes' in l:
        r = len(l['likes']['data'])
        likes_9.append(r)
    else:
        r = 0
        likes_9.append(r)


final_9_list = zip(emo,comments_9,likes_9)

outfile = open("emo_scores.csv","w")
outfile.write("emo_score, comment_counts, like_counts\n")

for a,b,c in final_9_list:
    outfile.write("{}, {}, {}\n".format(a,b,c))
outfile.close

print final_9_list

# Post a screenshot of your scatterplot to our facebook group!

# You can see what the scatterplot might look like
# in emo_scores.xlsx, included in the assignment. (In the example case, there's not an obvious correlation between positivity and how many comments or likes. There may not be, but you find that out by exploring the data!)


# Can you see any trends or possible relationships between likes, comments, and emo_scores? (Something to consider. Not graded.)



# OPTIONAL, but recommended for later: we will provide a folder in which you can upload all of your resulting CSV files, with a code file called compute_emo_relationships.py. That Python program will generate an aggregate CSV file with all of the data about emo_scores, comments, and likes to Facebook posts. If you run it inside the folder, it will generate a file 106W16_emo_patterns.csv, which you can import into Excel or upload to Google sheets to get a visual of associations between emo scores (by our definition), comments, and likes.






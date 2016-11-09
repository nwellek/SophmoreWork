# Advanced Accumulation Extra Credit
# SI 106: Programs, Information, and People - W16

# You will earn 25 points of extra credit for each rewrite of accumulation in advanced accumulation, up to 150 points (you cannot earn more than 150 points of extra credit from this EC assignment). To do this:

# - Find a code snippet from the textbook that uses the accumulation pattern. This may be an exercise, a successful answer to a problem set, an example. Code snippets that appear in the text or exercises for the Advanced Accumulation chapter are not eligible. Copy that code into this file. (See template below!)
# - Write a comment noting where it is in the textbook (the URL) and what the code is doing (very briefly, not more than one line).
# Rewrite the code using map, filter, a list comprehension, or reduce.

# Make sure this whole file runs! In any case where you are doing accumulation that deals with a file, you must provide a text file that will work for the mechanics. It need not be the same file we provided, but it can be.

# Your file will not be graded if it does not run. You will not receive any credit for incorrect advanced accumulation, if your new code does not do the same thing as the original code, or if you do not clearly provide where the original code came from so it is easy for us to find.

# Here's a template for each code bit (possible 25 points):

# Original code snippet below:
# <code here>
# Example: This is from Problem Set 4 #3, <url>. It creates a list of all of the words in the string s that are longer than 5 characters.
# New code with adv accumulation below:
# <code here>


#1 original code
numbers = [10, 20, 30, 40, 50]
#print numbers
for i in range(len(numbers)):
    numbers[i] = numbers[i]**2

print numbers
#This if from chp09_03b, https://www.programsinformationpeople.org/runestone/static/w16/Iteration/Listsandforloops.html, it takes the number and returns it to the power
numbers = [10, 20, 30, 40, 50]
print map(lambda x: x*x, numbers)


#2 original code
'''nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
accum = 0
for w in nums:
   accum = accum + w
print accum
'''
#This if from iter_accum1, https://www.programsinformationpeople.org/runestone/static/w16/Iteration/TheAccumulatorPattern.html, it takes a list of numbers and returns the sum of all the numbers in the list
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print sum(nums)


#3 original code
'''excited_words = ["hello!", "goodbye!", "wonderful!", "I love Python?"]

# Write your code here.
for a in excited_words:
	print a [:-1]
'''
#This if from ps_3_2, https://www.programsinformationpeople.org/runestone/static/w16/Assignments/ps3.html, it takes a list of words and prints them without the last character
excited_words = ["hello!", "goodbye!", "wonderful!", "I love Python?"]
print [words[:-1] for words in excited_words]


#4 original code
'''lp = ["hello","arachnophobia","lamplighter","inspirations","ice","amalgamation","programming","Python"]

# How many characters are in each element of list lp?
# Write code to print the length (number of characters)
for a in lp:
  print len(a)
'''
#This if from ps_3_6, https://www.programsinformationpeople.org/runestone/static/w16/Assignments/ps3.html, it takes a list of words and prints out the length of charatcers for each word
lp = ["hello","arachnophobia","lamplighter","inspirations","ice","amalgamation","programming","Python"]
print [len(x) for x in lp]



#5 original code
'''alist = [4,2,8,6,5]
blist = [ ]
for item in alist:
   blist.append(item+5)
   '''
#This if from exceptions-65, https://www.programsinformationpeople.org/runestone/static/w16/Iteration/TheAccumulatorPatternwithLists.html, it takes a list and returns it plus five
alist = [4,2,8,6,5]
print map(lambda x: x +5, alist)


#6 original code
'''
L = [3, 6, 2, 5, 39, 7, 5]
a = L[0]
for x in L[1:]:
	if x > a:
		a = x
print a
   '''
#This if from exceptions-65, https://www.programsinformationpeople.org/runestone/static/w16/Iteration/TheAccumulatorPatternwithLists.html, it takes a list and returns it plus five
L = [3, 6, 2, 5, 39, 7, 5]
print max(L)
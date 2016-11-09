import requests 
import test106 as test

def is_even(x):
	return x % 2 == 0

lst = [1, 2, 3, 4, 5, 6, 7, 8]
lst2 = [5, 10, 15, 20, 25, 30]
lst3 = [40, 50, 90, 100, 10, 30]
dct = {'nate': 95, "ben": 50, 'jon': 75, 'liz': 85, 'jeff': 100}
print filter(is_even, lst) #[2, 4, 6, 8]
print sorted(filter(is_even, lst), reverse =True) #[8, 6, 4, 2]
print filter(lambda x: x%2==0, lst) #[2, 4, 6, 8]

print map(is_even, lst) #[False, True, False, True, False, True, False, True]


def double(x):
	return x *2 

print map(double, lst) #2, 4, 6, 8, 10, 12, 14, 16]
print zip(lst, lst2) #(1, 5), (2, 10), (3, 15), (4, 20), (5, 25), (6, 30)]


print lambda x: lst *2 #<function <lambda> at 0x10fa6b500>
print sorted(lst3, key = lambda x: x) #[10, 30, 40, 50, 90, 100]

print sorted(dct, key = lambda x: x) #['ben', 'jeff', 'jon', 'liz', 'nate']
print sorted(dct, key = lambda x: dct[x]) #['ben', 'jon', 'liz', 'nate', 'jeff']
print sorted(dct, key = lambda x: dct[x], reverse = True) #'jeff', 'nate', 'liz', 'jon', 'ben']
#how do i print the value/ key and value
print "nate"[:-1]
def join_string(L, sep):
	string = ''
	for x in L:
		string = string + x + sep
	if sep == '':
		return string
	else:
		return string[:-1]
print join_string(['a', 'b', 'c'], '|')
print join_string(['a', 'b', 'c'], '')

L = ["Clear 40", 'All 99', "Beautiful 20", "Delightful 80"]
print sorted(L, reverse = True)

'''
def longest_strings(L):
	new_lst = []
	w = sorted(L, key = lambda x: len(x), reverse = True)
	for x in w(range(3)):
		new_lst.append(x)
	return new_lst

some_strings = ['a', 'abcd', 'ab', 'abc', 'abcde']
test.testEqual(longest_strings(some_strings), ['abcde', 'abcd', 'abc'])
'''









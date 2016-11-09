names = ["ben", 'nate', 'jon', 'carlos', 'jeff', 'liz', 'brady', 'mike', 'adam', 'jessica', 'david']
names_sorted = sorted (names)
print names_sorted
#this shows how to use the sorted function
names_sorted_reverse = sorted (names, reverse = True)
print names_sorted_reverse
#this is how to use sorted and then reverse
letter_values = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f':4, 'g': 2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':8, 'w':4, 'x':8, 'y':4, 'z':10}
word_scores = {}
for x in names:
	word_scores[x] = 0
	for l in x:
		word_scores[x] += letter_values[l]

best_name_top3 = []
for x in range (0,3):
	high_name = ""
	high_name_value = 0
	for i in word_scores:
		if word_scores[i] > high_name_value:
			high_name_value = word_scores[i]
			high_word = i 
	best_name_top3.append(high_word)
	del word_scores[high_word]
print best_name_top3
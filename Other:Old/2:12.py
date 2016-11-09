def common_char(strlst):
	chardict = {}
	for word in strlst:
		for ch in word:
			if ch not in chardict:
				chardict[ch] = 1
			else:
				chardict[ch] += 1

	keys = chardict.keys()
	most = chardict[keys[0]]
	mostkey = keys[0]
	for key in chardict:
		if chardict[key] > most:
			most = chardict[key]
			mostkey = key
	return mostkey

print common_char(["nate", "wellllllllllek", "is", "in", "106"])

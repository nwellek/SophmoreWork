import requests
import json
import billboard
chart = billboard.ChartData('hot-100')
#print chart
songs = []
for item in chart:
	songs.append(item.title)
print songs
print "These are the top 100 Billboard songs in order:"
start = 0
for song in chart:
	start += 1
	print str(start)+ ". " + song.title

print "These are the top 100 Billboard artist in order:"
start = 0
for song in chart:
	start += 1
	print str(start)+ ". " + song.artist

	
	



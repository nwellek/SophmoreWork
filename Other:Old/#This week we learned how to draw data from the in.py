#This week we learned how to draw data from the internet.  
#To do this we typically find a url (which is json format and convert it to python):

import requests
import json

url_parmameters = {"format": "json"}
#results = requests.get(<url>, params = url_parameters)
#python = results.json() #this turns it to python form
#since it is now in python form we can do many things
#such as find songs in tunes, temperature at airports, and really any data that we now have
# this is extremely useful since we are taking real stuff and now able to read it in a easier way
#and I now knwo how this is code

#in addition to drawing stuff from the interenet we also learned
#how to work with CSV's (creating excel sheets via code)
outfile = open("airport.csv","w") #airports reprensents the name of the file(excel name)
# we then give colums to the file
outfile.write("Temp, City, Conditions\n") #each comma breaks up the new colums
airports = ["ORD", "PHX", "JFK", "LGA", "DTW"]
for x in airports:
	w = extract_airport_data(x)
	utfile.write("{}\n".format(w))
outfile.close()

outfile = open('airport_temps.csv', 'w')



    

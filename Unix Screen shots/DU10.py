#this week we learned how to zip files together
#I have made two set of test scores and the zip them together
#I then took the average of the two 

test1 = [100, 80, 90, 93, 40, 88] #two 1 scores
test2 = [100, 76, 95, 87, 55, 92] #two 2 scores
testtotal = [] #blank list for total
test = zip(test1, test2) #method to zip together
 
for (x1, x2) in test: #iterate through each set of scores
   testtotal.append(x1+x2) #merging the scores together
   
print testtotal

testavg = [] #blank list for average
for x in testtotal: #iterate through total scores
  testavg.append (x/2) #dividing by 2 (number of tests)
print testavg #printing the average scores
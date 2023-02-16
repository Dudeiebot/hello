#f = open("/Users/Dudeiebeech/hello-1/bullish.txt", "r")
#for x in f:
 #   print(x)

#f = open("/Users/Dudeiebeech/hello-1/bullish.txt", "r")
#print(f.read(5))   

#kind of having issues here, have to debug before it run well, maybe i got to find out what is happening later on the day, for posterity it is in connection with opening a text file on python

#f = ("open.txt", "w")

import pandas
df = pandas.read_csv("/Users/Dudeiebeech/hello-1/data.csv")

print(df)
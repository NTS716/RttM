import sys
#writes to a text file called 'log.txt', logs information 
Log = open("./log.txt", "a")

def log(text):
	Log.write(text)

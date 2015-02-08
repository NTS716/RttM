import time, os
from inspect import getfile, currentframe
import __main__ as main
#writes to a text file called 'log.txt', logs information 
Log = open("./log.txt", "a")

def log(fileName ,message = "loaded with no errors"):
	currentFile = getfile(currentframe())
	currentPath = os.path.dirname(os.path.abspath(currentFile))
	currentTime = time.strftime("%D %I:%M:%S")
	if len(fileName) < 10:
		fileName = currentPath + "/" + fileName
	Log.write("\n" + currentTime + " - "  + fileName + " - " + message + "\n")

log(__file__)

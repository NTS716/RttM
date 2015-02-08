#Reads lines in a txt file called 'prefs.txt' and executes them as python code
Prefs = open("./prefs.txt")
for line in Prefs:
	exec(line)

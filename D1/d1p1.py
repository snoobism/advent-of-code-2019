import math
inputFile = open("d1input.txt", "r")
outputFile = open("d1output.txt", "w")

total = 0
for line in inputFile:
	total = total + math.floor(int(line)/3) - 2

outputFile.write(str(total))
import math

inputFile = open("d1input.txt", "r")
outputFile = open("d1p2output.txt", "w")

total = 0

def findFuel(mass, fuel):
	if math.floor(mass / 3) - 2 > 0:
		fuel += math.floor(mass / 3) - 2
		return findFuel(math.floor(mass / 3) - 2, fuel)
	else:
		return fuel

for line in inputFile:
	fuel = findFuel(int(line), 0)
	if fuel > 0:
		total = total + fuel

outputFile.write(str(total))
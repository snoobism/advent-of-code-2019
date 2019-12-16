fileInput = open("d3input.txt", "r")
fileOutput = open("d3p1output.txt", "w")

class Coord(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.d = 0
	def __str__(self):
		return "(" + str(self.x) + "," + str(self.y) + ")"

lineOne = [x.rstrip() for x in fileInput.readline().split(",")]
lineTwo = [x.rstrip() for x in fileInput.readline().split(",")]

wireOne = []
wireTwo = []

start = Coord(0, 0)
wireOne.append(start)
wireTwo.append(start)
currentDistance = 0

for i in range(0, len(lineOne)):
	if(lineOne[i][0] == "R"):
		wireOne.append(Coord(wireOne[i].x + int(lineOne[i][1:]), wireOne[i].y))
		currentDistance += int(lineOne[i][1:])
		wireOne[len(wireOne) - 1].d = currentDistance
	if(lineOne[i][0] == "L"):
		wireOne.append(Coord(wireOne[i].x - int(lineOne[i][1:]), wireOne[i].y))
		currentDistance += int(lineOne[i][1:])
		wireOne[len(wireOne) - 1].d = currentDistance
	if(lineOne[i][0] == "U"):
		wireOne.append(Coord(wireOne[i].x, wireOne[i].y + int(lineOne[i][1:])))
		currentDistance += int(lineOne[i][1:])
		wireOne[len(wireOne) - 1].d = currentDistance
	if(lineOne[i][0] == "D"):
		wireOne.append(Coord(wireOne[i].x, wireOne[i].y - int(lineOne[i][1:])))
		currentDistance += int(lineOne[i][1:])
		wireOne[len(wireOne) - 1].d = currentDistance

currentDistance = 0
for i in range(0, len(lineTwo)):
	if(lineTwo[i][0] == "R"):
		wireTwo.append(Coord(wireTwo[i].x + int(lineTwo[i][1:]), wireTwo[i].y))
		currentDistance += int(lineTwo[i][1:])
		wireTwo[len(wireTwo) - 1].d = currentDistance
	if(lineTwo[i][0] == "L"):
		wireTwo.append(Coord(wireTwo[i].x - int(lineTwo[i][1:]), wireTwo[i].y))
		currentDistance += int(lineTwo[i][1:])
		wireTwo[len(wireTwo) - 1].d = currentDistance
	if(lineTwo[i][0] == "U"):
		wireTwo.append(Coord(wireTwo[i].x, wireTwo[i].y + int(lineTwo[i][1:])))
		currentDistance += int(lineTwo[i][1:])
		wireTwo[len(wireTwo) - 1].d = currentDistance
	if(lineTwo[i][0] == "D"):
		wireTwo.append(Coord(wireTwo[i].x, wireTwo[i].y - int(lineTwo[i][1:])))
		currentDistance += int(lineTwo[i][1:])
		wireTwo[len(wireTwo) - 1].d = currentDistance

results = []
def checkIntersection(s1, e1, s2, e2): #start, end
	if s1.x == e1.x:
		if(s1.x > s2.x and s1.x < e2.x) or (s1.x < s2.x and s1.x > e2.x):
			return True
	elif s1.y == e1.y:
		if(s1.y > s2.y and s1.y < e2.y) or (s1.y < s2.y and s1.y > e2.y):
			return True

for i in range(0, len(wireTwo) - 1):
	for j in range(0, len(wireOne) - 1):
		if checkIntersection(wireTwo[i], wireTwo[i + 1], wireOne[j], wireOne[j + 1]) and checkIntersection(wireOne[j], wireOne[j + 1], wireTwo[i], wireTwo[i + 1]):
			if wireTwo[i].x == wireTwo[i + 1].x: # vertical
				results.append(Coord(wireTwo[i].x, wireOne[j].y))
				results[len(results) - 1].d = wireTwo[i].d + wireOne[j].d + abs(abs(results[len(results) - 1].y) - abs(wireTwo[i].y)) + abs(abs(results[len(results) - 1].x) - abs(wireOne[j].x)) 
			else: # orizontal
				results.append(Coord(wireOne[j].x, wireTwo[i].y))
				results[len(results) - 1].d = wireOne[i].d + wireTwo[j].d + abs(abs(results[len(results) - 1].y) - abs(wireOne[j].y)) + abs(abs(results[len(results) - 1].x) - abs(wireTwo[i].x)) 



minimumValue = 9999
minimumDist = float('inf')
for elem in results:
	if(abs(elem.x) + abs(elem.y) < minimumValue):
		minimumValue = abs(elem.x) + abs(elem.y)


for elem in results:
	if(elem.d < minimumDist):
		minimumDist = elem.d


for x in wireOne:
	print(x)
print(' ')
for x in wireTwo:
	print(x)
print(' ')
for x in results:
	print(x)

fileOutput.write(str(minimumValue))
fileOutput.write("\n")
fileOutput.write(str(minimumDist))

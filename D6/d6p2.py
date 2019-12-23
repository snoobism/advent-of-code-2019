fileInput = open("d6input.txt", "r")
fileOutput = open("d6p2output.txt", "w")

nodes = {}

for line in fileInput.read().splitlines():
	line = line.split(")")
	nodes[line[1]] = line[0]

count = 0

santaOrbits = []
node = "SAN" 
while node != "COM":
	node = nodes[node]
	santaOrbits.append(node)

youOrbits = []
node = "YOU"
while node != "COM":
	node = nodes[node]
	youOrbits.append(node)

for planet in santaOrbits:
	if planet in youOrbits:
		count = santaOrbits.index(planet) + youOrbits.index(planet)
		break

fileOutput.write(str(count))
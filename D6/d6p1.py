fileInput = open("d6input.txt", "r")
fileOutput = open("d6p1output.txt", "w")

nodes = {}

for line in fileInput.read().splitlines():
	line = line.split(")")
	nodes[line[1]] = line[0]

count = 0

for node in nodes:
	while(node != "COM"):
		count += 1
		node = nodes[node]

fileOutput.write(str(count))

fileInput = open("d8input.txt", "r")
fileOutput = open("d8p1output.txt", "w")

h = 6
w = 25

layerSize = h * w

minZero = 9999999999999
answer = 0

image = fileInput.readline()
for i in range(0, (len(image) - 1)//layerSize):
	zeroCount = 0
	oneCount = 0
	twoCount = 0

	for j in range(0, layerSize):
		pixel = int(image[layerSize * i + j]) 
		if pixel == 0:
			zeroCount += 1
		if pixel == 1:
			oneCount += 1
		if pixel == 2:
			twoCount += 1
	if zeroCount < minZero:
		minZero = zeroCount
		answer = oneCount * twoCount
fileOutput.write(str(answer))
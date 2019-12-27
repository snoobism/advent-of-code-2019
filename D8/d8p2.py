fileInput = open("d8input.txt", "r")
fileOutput = open("d8p2output.txt", "w")

h = 6
w = 25

layerSize = h * w

finalImage = [2 for _ in range(0,layerSize)]
image = fileInput.readline()
for i in range(0, (len(image) - 1)//layerSize):
	for j in range(0, layerSize):
		pixel = int(image[layerSize * i + j]) 
		if finalImage[j] == 2:
			finalImage[j] = pixel
fileOutput.write(str(finalImage))
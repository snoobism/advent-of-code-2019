inputFile = open("d2input.txt", "r")
outputFile = open("d2p1output.txt", "w")

opcode = [int(x) for x in inputFile.read().split(",")]

def add(inputOne, inputTwo, output):
	opcode[output] = opcode[inputOne] + opcode[inputTwo]

def mul(inputOne, inputTwo, output):
	opcode[output] = opcode[inputOne] * opcode[inputTwo]

def stop():
	outputFile.write(str(opcode[0]))
	exit(0)

index = 0
while(1):
	if opcode[index] == 1:
		add(opcode[index + 1], opcode[index + 2], opcode[index + 3])
	elif opcode[index] == 2:
		mul(opcode[index + 1], opcode[index + 2], opcode[index + 3])
	elif opcode[index] == 99:
		stop()
	else:
		exit(1)
	index += 4




inputFile = open("d2input.txt", "r") 
outputFile = open("d2p2output.txt", "w")

opcode = [int(x) for x in inputFile.read().split(",")]
opcodeConst = opcode.copy()

def add(inputOne, inputTwo, output):
	opcode[output] = opcode[inputOne] + opcode[inputTwo]

def mul(inputOne, inputTwo, output):
	opcode[output] = opcode[inputOne] * opcode[inputTwo]

def stop():
	return opcode[0]

for n in range(0, 100):
	for v in range(0, 100):
		index = 0
		opcode = opcodeConst.copy()
		opcode[1] = n
		opcode[2] = v
		while(1):
			if opcode[index] == 1:
				add(opcode[index + 1], opcode[index + 2], opcode[index + 3])
			elif opcode[index] == 2:
				mul(opcode[index + 1], opcode[index + 2], opcode[index + 3])
			elif opcode[index] == 99:
				if(stop() == 19690720):
					outputFile.write(str(n * 100 + v))
					exit(0)
				else:
					break;
			else:
				exit(1)
			index += 4

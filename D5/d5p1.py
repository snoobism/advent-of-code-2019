inputFile = open("d5input.txt", "r")
outputFile = open("d5p1output.txt", "w")

program = [int(x) for x in inputFile.read().split(",")]

def opcode(inp):
	code = [0, 0, 0, 0]
	code[3] = inp % 100
	code[2] = (inp // 100) % 10
	code[1] = (inp // 1000) % 10
	code[0] = (inp // 10000) % 10
	return code

def add(inputOne, inputTwo, output, modeOne, modeTwo):
	if modeOne == 1:
		inputOne = inputOne	# inputOne is in immediate mode
	else:
		inputOne = program[inputOne]

	if modeTwo == 1:
		inputTwo = inputTwo	# inputTwo is in immediate mode
	else:
		inputTwo = program[inputTwo]

	program[output] = inputOne + inputTwo

def mul(inputOne, inputTwo, output, modeOne, modeTwo):
	if modeOne == 1:
		inputOne = inputOne	# inputOne is in immediate mode
	else:
		inputOne = program[inputOne]

	if modeTwo == 1:
		inputTwo = inputTwo	# inputTwo is in immediate mode
	else:
		inputTwo = program[inputTwo]

	program[output] = inputOne * inputTwo

def inp(address):
	temp = input()
	program[address] = int(temp)

def wrt(address, mode):
	if mode == 0:
		outputFile.write(str(program[address]))
		outputFile.write("\n")
	else:
		outputFile.write(str(address))
		outputFile.write("\n")
		
def stop(): #halt
	exit(0)

index = 0
while(1):
	code = opcode(program[index])
	print(code)
	#print(program[index], index)
	if code[3] == 1:
		add(program[index + 1], program[index + 2], program[index + 3], code[2], code[1])
		index += 4
	elif code[3] == 2:
		mul(program[index + 1], program[index + 2], program[index + 3], code[2], code[1])
		index += 4
	elif code[3] == 3:
		inp(program[index + 1])
		index += 2
	elif code[3] == 4:
		wrt(program[index + 1], code[2])
		index += 2
	elif code[3] == 99:
		print("halt")
		stop()
	else:
		print("fatal error")
		exit(1)


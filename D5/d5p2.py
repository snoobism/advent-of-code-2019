inputFile = open("d5input.txt", "r")
outputFile = open("d5p2output.txt", "w")

program = [int(x) for x in inputFile.read().split(",")]

def opcode(inp):
	code = [0, 0, 0, 0]
	code[3] = inp % 100
	code[2] = (inp // 100) % 10
	code[1] = (inp // 1000) % 10
	code[0] = (inp // 10000) % 10
	return code

def add(inputOne, inputTwo, output, modeOne, modeTwo):
	global index
	if modeOne == 1:
		inputOne = inputOne	# inputOne is in immediate mode
	else:
		inputOne = program[inputOne]

	if modeTwo == 1:
		inputTwo = inputTwo	# inputTwo is in immediate mode
	else:
		inputTwo = program[inputTwo]

	program[output] = inputOne + inputTwo
	index += 4

def mul(inputOne, inputTwo, output, modeOne, modeTwo):
	global index
	if modeOne == 1:
		inputOne = inputOne	# inputOne is in immediate mode
	else:
		inputOne = program[inputOne]

	if modeTwo == 1:
		inputTwo = inputTwo	# inputTwo is in immediate mode
	else:
		inputTwo = program[inputTwo]

	program[output] = inputOne * inputTwo
	index += 4

def inp(address):
	global index
	temp = input()
	program[address] = int(temp)
	index += 2

def wrt(address, mode):
	global index
	if mode == 0:
		outputFile.write(str(program[address]))
		outputFile.write("\n")
	else:
		outputFile.write(str(address))
		outputFile.write("\n")
	index += 2
		
def jmpTrue(address, inputOne, inputTwo, modeOne, modeTwo):
	global index
	if modeOne == 1:
		if inputOne != 0:
			if modeTwo == 1:
				program[address] = inputTwo
			else:
				program[address] = program[inputTwo] 
			index = program[address]
		else:
			index += 3
	else:
		if program[inputOne] != 0:
			if modeTwo == 1:
				program[address] = inputTwo
			else:
				program[address] = program[inputTwo]
			index = program[address]
		else:
			index += 3

def jmpFalse(address, inputOne, inputTwo, modeOne, modeTwo):
	global index
	if modeOne == 1:
		if inputOne == 0:
			if modeTwo == 1:
				program[address] = inputTwo
			else:
				program[address] = program[inputTwo] 
			index = program[address]
		else:
			index += 3
	else:
		if program[inputOne] == 0:
			if modeTwo == 1:
				program[address] = inputTwo
			else:
				program[address] = program[inputTwo]
			index = program[address]
		else:
			index += 3

def less(inputOne, inputTwo, output, modeOne, modeTwo):
	global index
	if modeOne == 0:
		if modeTwo == 0:
			if program[inputOne] < program[inputTwo]:
				program[output] = 1
			else:
				program[output] = 0
		if modeTwo == 1:
			if program[inputOne] < inputTwo:
				program[output] = 1
			else:
				program[output] = 0
	else:
		if modeTwo == 0:
			if inputOne < program[inputTwo]:
				program[output] = 1
			else:
				program[output] = 0
		if modeTwo == 1:
			if inputOne < inputTwo:
				program[output] = 1
			else:
				program[output] = 0
	index += 4

def equal(inputOne, inputTwo, output, modeOne, modeTwo):
	global index
	if modeOne == 0:
		if modeTwo == 0:
			print(inputOne, inputTwo, output)
			if program[inputOne] == program[inputTwo]:
				program[output] = 1
			else:
				program[output] = 0
		if modeTwo == 1:
			if program[inputOne] == inputTwo:
				program[output] = 1
			else:
				program[output] = 0
	else:
		if modeTwo == 0:
			if inputOne == program[inputTwo]:
				program[output] = 1
			else:
				program[output] = 0
		if modeTwo == 1:
			if inputOne == inputTwo:
				program[output] = 1
			else:
				program[output] = 0
	index += 4

def stop(): #halt
	exit(0)
global index
index = 0
while(1):
	code = opcode(program[index])
	print(code)
	#print(program[index], index)
	if code[3] == 1:
		add(program[index + 1], program[index + 2], program[index + 3], code[2], code[1])
	elif code[3] == 2:
		mul(program[index + 1], program[index + 2], program[index + 3], code[2], code[1])
	elif code[3] == 3:
		inp(program[index + 1])
	elif code[3] == 4:
		wrt(program[index + 1], code[2])
	elif code[3] == 5:
		jmpTrue(index, program[index + 1], program[index + 2], code[2], code[1])
	elif code[3] == 6:
		jmpFalse(index, program[index + 1], program[index + 2], code[2], code[1])
	elif code[3] == 7:
		less(program[index + 1], program[index + 2], program[index + 3], code[2], code[1])
	elif code[3] == 8:
		equal(program[index + 1], program[index + 2], program[index + 3], code[2], code[1])
	elif code[3] == 99:
		print("halt")
		stop()
	else:
		print("fatal error")
		exit(1)


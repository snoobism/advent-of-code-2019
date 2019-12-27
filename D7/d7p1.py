import sys

inputFile = open("d7input.txt", "r")
outputFile = open("d7p1output.txt", "w")

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

def inp(address, val):
	global index
	#temp = input()
	temp = val
	program[address] = int(temp)
	index += 2

def wrt(address, mode):
	global index
	index += 2

	if mode == 0:
		return program[address]
	else:
		return address
		
def jmpTrue(address, inputOne, inputTwo, modeOne, modeTwo):
	global index
	if modeOne == 1:
		if inputOne != 0:
			if modeTwo == 1:
				index = inputTwo
			else:
				index = program[inputTwo] 
			#index = program[address]
		else:
			index += 3
	else:
		if program[inputOne] != 0:
			if modeTwo == 1:
				index = inputTwo
			else:
				index = program[inputTwo] 
			#index = program[address]
		else:
			index += 3

def jmpFalse(address, inputOne, inputTwo, modeOne, modeTwo):
	global index
	if modeOne == 1:
		if inputOne == 0:
			if modeTwo == 1:
				index = inputTwo
			else:
				index = program[inputTwo] 
			#index = program[address]
		else:
			index += 3
	else:
		if program[inputOne] == 0:
			if modeTwo == 1:
				index = inputTwo
			else:
				index = program[inputTwo] 
			#index = program[address]
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
	#exit(0)
	#return value
	print("halt")
values = []

def generatePermutations(A, size, n):
	if size == 1:
		values.append(list(A))

	for i in range(0, size):
		generatePermutations(A, size - 1, n)
		if size % 2 == 1:
			temp = A[0]
			A[0] = A[size - 1]
			A[size - 1] = temp
		else:
			temp = A[i]
			A[i] = A[size - 1]
			A[size - 1] = temp



def main(phase, value):
	global index
	index = 0
	inputOne = True
	while(1):
		code = opcode(program[index])
		if code[3] == 1:
			add(program[index + 1], program[index + 2], program[index + 3], code[2], code[1])
		elif code[3] == 2:
			mul(program[index + 1], program[index + 2], program[index + 3], code[2], code[1])
		elif code[3] == 3:
			if inputOne == True:
				inputOne = False
				inp(program[index + 1], phase)
			else:
				inp(program[index + 1], value)
		elif code[3] == 4:
			return wrt(program[index + 1], code[2])
		elif code[3] == 5:
			jmpTrue(index, program[index + 1], program[index + 2], code[2], code[1])
		elif code[3] == 6:
			jmpFalse(index, program[index + 1], program[index + 2], code[2], code[1])
		elif code[3] == 7:
			less(program[index + 1], program[index + 2], program[index + 3], code[2], code[1])
		elif code[3] == 8:
			equal(program[index + 1], program[index + 2], program[index + 3], code[2], code[1])
		elif code[3] == 99:
			#exit(0)
			stop()
		else:
			print("fatal error")
			exit(1)

maxValue = 0

generatePermutations([0, 1, 2, 3, 4], 5, 5)
print(values)
phases = []

for permutation in values:
	signal = main(permutation[4], main(permutation[3], main(permutation[2], main(permutation[1], main(permutation[0], 0)))))
	if signal > maxValue:
		maxValue = signal
		phases = permutation
outputFile.write(str(maxValue))

import sys

inputFile = open("d7input.txt", "r")
outputFile = open("d7p2output.txt", "w")


class CPU(object):
	def __init__(self, name):
		self.index = 0
		self.phaseInput = True
		self.name = name
		self.halted = False
		inputFile.seek(0, 0)
		self.program = [int(x) for x in inputFile.read().split(",")]


	def __str__(self):
		return self.name

	def opcode(self, inp):
		code = [0, 0, 0, 0]
		code[3] = inp % 100
		code[2] = (inp // 100) % 10
		code[1] = (inp // 1000) % 10
		code[0] = (inp // 10000) % 10
		return code

	def add(self, inputOne, inputTwo, output, modeOne, modeTwo):
		if modeOne == 1:
			inputOne = inputOne	# inputOne is in immediate mode
		else:
			inputOne = self.program[inputOne]

		if modeTwo == 1:
			inputTwo = inputTwo	# inputTwo is in immediate mode
		else:
			inputTwo = self.program[inputTwo]

		self.program[output] = inputOne + inputTwo
		self.index += 4

	def mul(self, inputOne, inputTwo, output, modeOne, modeTwo):
		if modeOne == 1:
			inputOne = inputOne	# inputOne is in immediate mode
		else:
			inputOne = self.program[inputOne]

		if modeTwo == 1:
			inputTwo = inputTwo	# inputTwo is in immediate mode
		else:
			inputTwo = self.program[inputTwo]

		self.program[output] = inputOne * inputTwo
		self.index += 4

	def inp(self, address, val):
		#temp = input()
		temp = val
		self.program[address] = int(temp)
		self.index += 2

	def wrt(self, address, mode):
		self.index += 2

		if mode == 0:
			return self.program[address]
		else:
			return address
			
	def jmpTrue(self, address, inputOne, inputTwo, modeOne, modeTwo):
		if modeOne == 1:
			if inputOne != 0:
				if modeTwo == 1:
					self.index = inputTwo
				else:
					self.index = self.program[inputTwo] 
				#self.index = self.program[address]
			else:
				self.index += 3
		else:
			if self.program[inputOne] != 0:
				if modeTwo == 1:
					self.index = inputTwo
				else:
					self.index = self.program[inputTwo] 
				#self.index = self.program[address]
			else:
				self.index += 3

	def jmpFalse(self, address, inputOne, inputTwo, modeOne, modeTwo):
		if modeOne == 1:
			if inputOne == 0:
				if modeTwo == 1:
					self.index = inputTwo
				else:
					self.index = self.program[inputTwo] 
				#self.index = self.program[address]
			else:
				self.index += 3
		else:
			if self.program[inputOne] == 0:
				if modeTwo == 1:
					self.index = inputTwo
				else:
					self.index = self.program[inputTwo] 
				#self.index = self.program[address]
			else:
				self.index += 3

	def less(self, inputOne, inputTwo, output, modeOne, modeTwo):
		if modeOne == 0:
			if modeTwo == 0:
				if self.program[inputOne] < self.program[inputTwo]:
					self.program[output] = 1
				else:
					self.program[output] = 0
			if modeTwo == 1:
				if self.program[inputOne] < inputTwo:
					self.program[output] = 1
				else:
					self.program[output] = 0
		else:
			if modeTwo == 0:
				if inputOne < self.program[inputTwo]:
					self.program[output] = 1
				else:
					self.program[output] = 0
			if modeTwo == 1:
				if inputOne < inputTwo:
					self.program[output] = 1
				else:
					self.program[output] = 0
		self.index += 4

	def equal(self, inputOne, inputTwo, output, modeOne, modeTwo):
		if modeOne == 0:
			if modeTwo == 0:
				if self.program[inputOne] == self.program[inputTwo]:
					self.program[output] = 1
				else:
					self.program[output] = 0
			if modeTwo == 1:
				if self.program[inputOne] == inputTwo:
					self.program[output] = 1
				else:
					self.program[output] = 0
		else:
			if modeTwo == 0:
				if inputOne == self.program[inputTwo]:
					self.program[output] = 1
				else:
					self.program[output] = 0
			if modeTwo == 1:
				if inputOne == inputTwo:
					self.program[output] = 1
				else:
					self.program[output] = 0
		self.index += 4

	def stop(self, value): #halt
		#exit(0)
		#return value
		print("halt")
		self.halted = True
		return value

	def reset(self):
		self.halted = False
		self.phaseInput = True
		self.index = 0
		inputFile.seek(0, 0)
		self.program = [int(x) for x in inputFile.read().split(",")]

	def main(self, phase, value):
		while(1):
			print(self)
			code = self.opcode(self.program[self.index])
			#print(code)
			#print(self.program[self.index], self.index)
			if code[3] == 1:
				self.add(self.program[self.index + 1], self.program[self.index + 2], self.program[self.index + 3], code[2], code[1])
			elif code[3] == 2:
				self.mul(self.program[self.index + 1], self.program[self.index + 2], self.program[self.index + 3], code[2], code[1])
			elif code[3] == 3:
				if self.phaseInput == True:
					self.phaseInput = False
					self.inp(self.program[self.index + 1], phase)
				else:
					self.inp(self.program[self.index + 1], value)
			elif code[3] == 4:
				return self.wrt(self.program[self.index + 1], code[2])
			elif code[3] == 5:
				self.jmpTrue(self.index, self.program[self.index + 1], self.program[self.index + 2], code[2], code[1])
			elif code[3] == 6:
				self.jmpFalse(self.index, self.program[self.index + 1], self.program[self.index + 2], code[2], code[1])
			elif code[3] == 7:
				self.less(self.program[self.index + 1], self.program[self.index + 2], self.program[self.index + 3], code[2], code[1])
			elif code[3] == 8:
				self.equal(self.program[self.index + 1], self.program[self.index + 2], self.program[self.index + 3], code[2], code[1])
			elif code[3] == 99:
				#exit(0)
				return self.stop(value)
			else:
				print("fatal error")
				exit(1)

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

maxValue = 0
values = []
A, B, C, D, E = CPU("A"), CPU("B"), CPU("C"), CPU("D"), CPU("E")
generatePermutations([5, 6, 7, 8, 9], 5, 5)
phases = []
for permutation in values:
	signal = 0

	A.reset()
	B.reset()
	C.reset()
	D.reset()
	E.reset()

	while A.halted == False and B.halted == False and C.halted == False and D.halted == False and E.halted == False:
		signal = A.main(permutation[0], signal)
		signal = B.main(permutation[1], signal)
		signal = C.main(permutation[2], signal)
		signal = D.main(permutation[3], signal)
		signal = E.main(permutation[4], signal)

	if signal > maxValue:
		maxValue = signal
		phases = permutation
outputFile.write(str(maxValue))

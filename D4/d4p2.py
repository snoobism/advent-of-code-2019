start = 172851
end = 675869

solutions = 0
digits = [0, 0, 0, 0, 0, 0]
validSolution = True

for i in range(start, end + 1):
	validSolution = True
	ok = False
	for j in range(0, 6):
		digits[j] = i // 10**(5-j) % 10
	for j in range(0, 5):
		if digits[j] > digits[j + 1]:
			validSolution = False
	if digits[0] == digits[1] and digits[1] != digits[2]:
		ok = True
	for j in range(1, 4):
		if digits[j-1] != digits[j] and digits[j] == digits[j + 1] and digits[j + 1] != digits[j + 2]:
			ok = True
	if digits[3] != digits[4] and digits[4] == digits[5]:
		ok = True
	if validSolution == True and ok == True:
		solutions += 1
		print(i)

print(solutions)

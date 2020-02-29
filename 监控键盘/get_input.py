buf = []

with open('keylogger.txt', 'r')as file:
	for line in file:
		buf += line[-3]
	print(buf)
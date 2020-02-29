import os
import time
import win32process


print('reading log, p1 start!')

while True:
	if int(time.time())%10 == 0:
		print('write log')
		with open('log.txt', 'w') as f:
			f.write(str(time.time()))
			


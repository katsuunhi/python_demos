import os
import time
import win32process
import psutil

handle = win32process.CreateProcess('p1.exe','', None , None , 0 ,win32process. CREATE_NO_WINDOW , None , None ,win32process.STARTUPINFO())

while True:
	time.sleep(10)
	try:
		p = psutil.Process(handle[2])
		print(p.status)
	except:
		handle = win32process.CreateProcess('p1.exe','', None , None , 0 ,win32process. CREATE_NO_WINDOW , None , None ,win32process.STARTUPINFO())
		print('restart p1')
		p = psutil.Process(handle[2])
		print(p.status)

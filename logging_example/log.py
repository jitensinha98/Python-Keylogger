import logging
logging.basicConfig(filename='test.log',level=logging.DEBUG)
def print_name():
	z=str(raw_input("ENTER YOUR NAME : "))
	return z;

my_name=print_name()
logging.debug(my_name)	
#print my_name

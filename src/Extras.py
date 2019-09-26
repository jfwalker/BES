from datetime import datetime
import sys
import os

'''
Set of extra stuff, not essential for functions
'''


#Basic time thingy
def get_time(position, outfile):
	now = datetime.now()
	dt_string = now.strftime("%B %d, %Y %H:%M:%S")
	if outfile:
		print position + " " + dt_string
		outfile.write(position + " " + dt_string + "\n")
	else:
		print position + " " + dt_string

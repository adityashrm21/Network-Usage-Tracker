#!/usr/bin/env python


import os
import sys
import time
#import re
import threading
import subprocess


def monitor(limit, unit):
	#threading.Timer(4.0, monitor).start()
	check="vnstat"
	#os.system(check)
  	proc=subprocess.Popen(check, shell=True, stdout=subprocess.PIPE)
  	output=proc.communicate()
  	output=str(output)
  	print output
  	l = []
	for t in output.split():
		try:
			if t=="MiB" or t=="GiB":
				l.append(t)
			else:
				l.append(float(t))
			
		except ValueError:
			pass
	print l
	if unit==l[5] and limit<l[4]:
		print "\nnetwork usage limit exceeded!\n"


#def callMonitor(limit, unit):
#	threading.Timer(4.0, callMonitor).start()
#	monitor(limit, unit)
	

def main():
	if len(sys.argv) >3 or len(sys.argv)<3:
		print 'command usage: python bandwidth.py <data usage in MiB or GiB>'
		print 'example: python bandwidth.py 500 MiB'
		print 'or python bandwidth.py 2 GiB'
		exit(1)
	else:
		limit=float(sys.argv[1])
		unit=str(sys.argv[2])

		#callMonitor(limit, unit)
		monitor(limit, unit)



if __name__ == '__main__':
	main()
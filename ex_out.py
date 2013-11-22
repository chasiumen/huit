#!/usr/bin/python
#Author: Ryosuke Morino
#Description: output Switch model, Chassis Seiral, Blade model, blade serial
#
#	ex_out	+------> output to Screen
#			|	
#			|	
#		 	+-----src/get_switch_info.py //retrive switch info (show ver, show mod)
#			|			|
#			|			+-------temp.txt  //output of get_switch_info.py
#			|					   
#			+---------------src/serial_finder.py 	//get SNs from temp.txt
#									


import sys, re, subprocess


if len(sys.argv) != 2:
	print "Error! Usage: ./ex_out.py HOSTNAME"
	sys.exit()
else:

	cmd0='/Users/leox/huit/src/get_switch_info.py ' + sys.argv[1] 
	cmd1='/Users/leox/huit/src/get_switch_info.py ' + sys.argv[1] + ' > temp.txt'
	cmd2='/Users/leox/huit/src/serial_finder.py temp.txt'

#	print cmd1, "cmd1"
#	print cmd2, "cmd2"

	subprocess.call(cmd0, shell=True)
	print "################################################################################\n"
	print "Processing.....\n\n\n\n"
	subprocess.call(cmd1, shell=True)
	print sys.argv[1]
	subprocess.call(cmd2, shell=True)
	

#!/usr/bin/python
#Author: Ryosuke Morino

#---------------WARNING----------------------
#This script is only dedicated to stackable 3500X serise
#
#
#	3750_out.py	+------> output to Screen
#           	|   
#           	|   
#          		+-----src/3750_get_info.py //retrive switch info (show ver, show mod, etc...)
#          		|           |
#          		|           +-------temp.txt  //output of get_switch_info.py
#          		|                      
#          		+---------------src/3750_serial.py    //get SNs from temp.txt
#

import sys, re, subprocess


if len(sys.argv) != 2:
	print "Error! Usage: ./3750_out.py HOSTNAME"
	sys.exit()

else:
	cmd1='/Users/leox/huit/src/3750_get_info.py ' + sys.argv[1]
	cmd2='/Users/leox/huit/src/3750_get_info.py ' + sys.argv[1] + ' > temp_3750.txt'
	cmd3='/Users/leox/huit/src/3750_serial.py temp_3750.txt'

	subprocess.call(cmd1, shell=True)
	print "################################################################################\n"

	print "Processing.....\n\n\n\n"
	subprocess.call(cmd2, shell=True)
	subprocess.call(cmd3, shell=True)


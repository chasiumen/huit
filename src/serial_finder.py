#!/usr/bin/python
#
#
#---------------WARNING----------------------
#This script is only dedicated to 6500 serise
#get switch model, blade model
#Author: Ryosuke Morino



import sys, re, subprocess

#FUNCTION: get chassis info (model and SN)
def chassis(line, model , sn):
	#print x
	#get chassis model number
	if re.search(r"cisco WS-C\d{4}\w{,2}", line):
		#print line, "[original]"
		line = re.split("\s", line)
		model.append(line[1])
		#chassis model
		#print model
	#get chassis Serial number
	elif re.search(r"Processor board ID \w{11}", line):
#		print line, "[chassis SN]"
		line = re.split("\s", line)
		sn.append(line[3])	
		#print sn
		return(line, model, sn)
	else:
		return(line)


#FUNCTION: get blades info (model and SN)
def blades(line, model, sn):
	if re.search(r"WS-([a-z]|[A-Z]|\d){,6}-([a-z]|[A-Z]|\d){2,3}", line):
		#print line, "blades"
		if re.search(r"(Module|\(Active\)|\s+SFP|RJ45|Ethernet|\(Hot\)|\(?SFP\+\)?\s+)", line):	
			line = re.split(r"(Module|\(Active\)|\s+SFP|mb\sRJ45|Ethernet|\(Hot\)|\(?SFP\+\)?)",line)
		#	print line
			line = re.split("\s+", line[2])
		#blades model name
			model.append(line[1])
			#print line[1], "Blade_model"
		#baldes SN
			sn.append(line[2])
			#print line[2], "Blade_SN"
			return(line, model, sn)
		else:
			pass
	else:
		return(line)

def a_out(array, c):
	c = 0
	for x in array:
		print x
		c += 1
	return(c)


#check number of arguments
if len(sys.argv) != 2:
	print "Error! Usage: ./serial_finder FILE"
	sys.exit()

else:
#----------------MAIN---------------------
#initialize variabels
#	input: input file from commadline arguemnt
#	chassis_model: model number of the chassis
#	chassis_sn:	   SN of the chassis
#	blades_model: blades model array
#	blades_sn: blades  SN array
	input = sys.argv[1]
	chassis_model = []
	chassis_sn = []
	blades_model = []
	blades_sn = []
	c = 0	

	try:
		#open input file
		fin = open (input, "r")
	except IOError:
		print "couldn't open" , input
		sys.exit()
	
	#read
	line = fin.readline()
	while line:
		#print line
		
	#get chassis info
		chassis(line, chassis_model, chassis_sn)
	#get blades info
		blades(line, blades_model, blades_sn)
		line = fin.readline()
	fin.close()

#Output
	print "----------------CHASSIS----------------\n"
	a_out(chassis_model,c)
	a_out(chassis_sn,c)

	
	print "\n--------------LINECARDS----------------\n"
	
	print "Model:"
	blade_c = a_out(blades_model,c)
	print "[" , blade_c , "]\n"
	
	print "Serial Number:"
	blade_sn = a_out(blades_sn,c )
	print "[", blade_sn ,"]\n"


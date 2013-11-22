#!/usr/bin/python
#
#
#---------------WARNING----------------------
#This script is only dedicated to stackable 3500X serise
#get switch model, blade model
#Author: Ryosuke Morino



import sys, re, subprocess

#FUNCTION: get chassis info (model and SN)
def switch_info(line, ip, mac, model, sn, name):
	#get hostname
	if re.search(r">show ver", line):
		line_host = re.split(r">", line)
		name.append(line_host[0])
		#print line_host[0]

	#get ip address
	if re.search(r"Vlan((\d){2})\s+", line):
		line_ip = re.split("(([0-9]{1,3}\.){3}([0-9]{1,3}))", line)
		ip.append(line_ip[1])
		#print line_ip[1]

	#get MAC address
	if re.search(r"Internet\s+", line):	
		line_mac = re.split("(([0-9a-f]{4}\.){2}([0-9a-f]{4}))", line)
		#print line_mac[1]
		mac.append(line_mac[1])


	#get chassis model number
	if re.search(r"Model number\s+:", line):
		line_model = re.split("\s+:\s", line)
		line_model = line_model[1].strip('\n')
		model.append(line_model)
		#print line_model
	#get chassis Serial number
	elif re.search(r"System serial number\s+:", line):
		line_sn = re.split("\s+:\s", line)
		line_sn = line_sn[1].strip('\n')
		sn.append(line_sn)
		#print line_sn
		return(line, ip, mac, model, sn, name)
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
#	mac:	MAC address array

	input = sys.argv[1]
	hostname = []
	blades_model = []
	blades_sn = []
	mac = []
	ip = []
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
		
	#get switch info
		switch_info(line, ip, mac, blades_model, blades_sn, hostname)
	#get MAC address info

	#get IP
		line = fin.readline()
	fin.close()

#Output
	print "----------------CHASSIS----------------\n"
	print mac[0]
	print hostname[0]
	print blades_model[0]
	print blades_sn[0]
	print ip[0]
	
	print "\n--------------LINECARDS----------------\n"
	
	print "Model:"
	blade_c = a_out(blades_model,c)
	print "[" , blade_c , "]\n"
	
	print "Serial Number:"
	blade_sn = a_out(blades_sn,c )
	print "[", blade_sn ,"]\n"


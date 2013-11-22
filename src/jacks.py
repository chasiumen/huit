#!/usr/bin/python
#get jack and port infromation
import sys, re, subprocess, os

#adjust this if the script does not work
#array size for device name 
dev_len = 2




#FUNCTION: find jack numbers
def f_search(x, a_jack, a_slot, a_port, a_vlan, dev_len):
	x = x.strip()
	#print x
	x = re.split("\s+", x)

#total length of array to check only importatnt info
	if len(x) <= 25:
		#print x
		pass
	else:
		#print x
	#JACK
		#13th element in the array
		jack = x[12]
		a_jack.append(jack)
		#print "[JACK]", jack

	#SLOT	
		#compute jacks + dev_name
		n = 12+dev_len+1
		#x[15]
		sp = re.split("/", x[n])

		slot =  sp[1]
		a_slot.append(slot)
		#print "[SLOT]", slot, 
	#PORT
		port = sp[2]
		a_port.append(port)
		#print "[PORT]", port,

	#VLAN
		vlan = x[n+1]	
		a_vlan.append(vlan)
		#print "[VLAN]", vlan
	
		return(line)

#Jack	Room	Closet	Media Type	Device	Slot	Port	VLAN

def f_out(jack, slot, port, vlan, c):
	c = 0
	if len(jack) == len(slot) and len(slot) == len(port) and len(port) == len(vlan):
		for i in range(0, len(jack)):
			print jack[i],",",
			print ",", #Room
			print ",", #Closet
			print ",", #Media_Type
			print device, ",", #Device
			print slot[i],",",
			print port[i],",",
			print vlan[i]
			c += 1
		return (c)
	else:
		print "Error! The array length is not same."
		sys.exit()





if len(sys.argv) != 2:
	print "Error! Usage: ./jacks.py INPUT_FILE"
else:
#--------------MAIN------------------
	#VARIABLES
	#in_file:	input file
	#c:			coutner

	device = raw_input("Name of the switch?>")
	

	in_file = sys.argv[1] 	
	#ARRAYS
	#	jack
	#	slot
	#	port
	#	vlan
	a_jack = []
	a_slot = []
	a_port = []
	a_vlan = []

	c = 0
	try:
		#open input file
		fin = open(in_file, "r")
	except IOError:
		print "couldn't open", in_file
		sys.exit()

	#read/write
	line = fin.readline()
	while line:
		f_search(line, a_jack, a_slot, a_port, a_vlan, dev_len)
		line = fin.readline()

	fin.close()


#output
	print f_out(a_jack, a_slot, a_port, a_vlan, c)


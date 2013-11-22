#!/usr/bin/python
#
#------------For Cat 3750---------------

#description: this scripts use Pexpect to login to netops
#retreve output info of 'show ver' and 'show module'
#Author: Ryosuke Morino

import sys, pexpect, base64


#Function: Login process
def process(login, hash):
	dehash = base64.b64decode(hash)
	login.sendline(dehash)	
	return(login)
	
def cmds(login):
#show version
#	MAC address
#	IP address
#	Model number
#	Serial number

	login.sendline('show ver | inc Base ethernet')
	#login.expect(' *.>.*')
	login.sendline('show ip interface brief | inc Vlan')
	
	login.sendline('show arp')
	login.sendline('show ver | inc Model number')
	login.sendline('show ver | inc System serial')
	
	login.sendline('exit')
	login.interact()
	return(login)

#---------MAIN---------------
if __name__ == '__main__':

	if len(sys.argv) != 2:
		print "Error! Usage: ./netops.py HOSTNAME"		
		sys.exit()
	else:
	#Initialize Varibles
		user = "rmorino"
		hash = "YWd1bWlvbiQwODIy"
		server = sys.argv[1]
		outfile ="/Users/leox/huit/out.txt"

	#SSH Login
		login = pexpect.spawn('ssh %s@%s' %(user, server))
	#check RSA fingerprint
		print "Login processing..."
		c = login.expect(["Are you sure you want to continue connecting", '.assword:', pexpect.EOF])

	#add to KnownHosts: send yes and login
		if c == 0:
			#print "C", c
			login.sendline("yes")	
			login.expect('.sword:*')    
			process(login, hash)
			print "logged in!"
			cmds(login)

	#KnownHosts: just login
		elif c == 1:
			#print "C", c
			#login.expect('.sword:*')    
			process(login, hash)
			print "Logged in!"
			cmds(login)

		else:
			print "Error: login failed!"
			sys.exit()


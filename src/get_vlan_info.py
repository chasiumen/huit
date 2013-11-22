#!/usr/bin/python
#description: this scripts use Pexpect to login to netops
#retreve output info of 'show ver' and 'show module'
#Author: Ryosuke Morino

import sys, pexpect, base64


#Function: Login process
def process(login, hash):
	dehash = base64.b64decode(hash)
	login.sendline(dehash)	
	return(login)

#FUNCTION: send commands	
def cmds(login):
	#show version
	login.sendline('show int status')
	login.expect(" --More-- ")
	login.sendline(" ")
	login.expect(" --More-- ")
	login.sendline(" ")
	

#	login.expect ('.*More.*')
#	login.sendline(" ")
	login.sendline('exit')
	login.interact()



	
#	#show module
#	login.sendline('show mod')
#	login.sendline(" ")
#	login.sendline('exit')
#	login.interact()



#---------MAIN---------------
if __name__ == '__main__':

	if len(sys.argv) != 2:
		print "Error! Usage: ./get_vlan_info.py HOSTNAME"		
		sys.exit()

	else:
		#Initialize Varibles
		user = "rmorino"
		hash = "YWd1bWlvbiQwODIy"
		server = sys.argv[1]
		
		login = pexpect.spawn('ssh %s@%s' %(user, server))
		#check RSA fingerprint
		c = login.expect(["Are you sure you want to continue connecting", '.assword:', pexpect.EOF], timeout=20 )
		
		#send yes
		if c == 0:
			print "C", c
			print "Login Processing..."
			login.sendline("yes")	
			login.expect('.sword:*')    
			process(login, hash)
			print "Login!"
			cmds(login)	
	
		#known host just login
		elif c == 1:
			print "C", c
			print "Login Processing..."
			#login.expect('.sword:*')    
			process(login, hash)
			print "Login!"
			cmds(login)
		else:
			sys.exit()


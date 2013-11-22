#!/usr/bin/python

from Exscript.util.interact import read_login
from Exscript.protocols import SSH2
account = "rmorino"
server = "lamont-d-sw"


account = read_login()              
conn = SSH2()                       
conn.connect(server)     
conn.login(account)  

conn.execute('terminal length 0')           

conn.execute('show version')
print conn.response

conn.send('exit\r')               
conn.close()  

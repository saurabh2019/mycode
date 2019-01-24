#!/usr/bin/env python3
##try a real worl test with getpass

#import paramiko so we can ssh
import os #low level operating system commands
import getpass #We need this to accept passwords
import paramiko #allows python to ssh

#Where to connect to
t = paramiko.Transport("10.10.2.3",22) ## IP and port of bender

# how to connect 
t.connect(username="bender",password=getpass.getpass())

##Make an sftp connection object
sftp = paramiko.SFTPClient.from_transport(t)

##copy our firstpass.py script to bender
sftp.put("firstpasswd.py","firstpasswd.py") #move file to target location

##close the connection
sftp.close() #close the connection

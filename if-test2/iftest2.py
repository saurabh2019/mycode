#!/usr/bin/env python3
ipchk = input('Apply an IP address: ') # this line now prompts the user for input

if ipchk == '192.168.70.1': # if any data is provided, this will test true
   print('Looks like the gateway IP address was set: ' + ipchk) # indented under if
elif ipchk:
   print('Looks like the IP address was set: ' + ipchk )
else:#if Data is not provided
   print('You did not provide any data or input')


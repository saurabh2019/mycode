#!/usr/bin/env python3

## create a dictionary
switch = {'hostname': 'sw1', 'ip': '10.0.1.1', 'version': '1.2', 'vendor': 'cisco'}

## display parts of the dictionary
print( switch.get('hostname') )
print( switch['ip'] )

## request a 'fake' key
#print( switch.get('lynx') )  

#request a fake key with .get() method
print("first test - .get()")
print(switch.get('lynx'))

print( "Second test - .get()" )
print( switch.get('lynx',"the key is in another catsle!"))

print("Third test - .get()")
print(  switch.get('version'))

print("Fourth Test - .keys()")
print( switch.keys())

print ("Fifth test - .values()")
print (switch.values())

print ( "Sixth test - .pop()" )
switch.pop('version') #removes this key (and value)pair
print( switch.keys() )#notice the value of version is gone
print( switch.values() ) #notice the value of 1.2

print ( "Seventh Test - Add a new value" )
switch['adminlogin']='karl09'
print( switch.keys() )
print( switch.values() )

print( "Eighth test - ADD a new value" )
switch['password'] = 'qwerty'
print( switch.keys() )
print( switch.values() )

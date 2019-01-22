#!/usr/bin/env python3

listofvendors = ['cisco','juniper','big_ip','f5','arsita']

for vendor in listofvendors:
	print(vendor)

##userinput
userinput = input("What are you looking for ?")

##test for inclusion (no loop required)
if userinput in listofvendors :
	print('yeah we support the venodor') 
else:
	print('We don\'t support vendor')

mylist = []
for x in range(0,101):
	mylist.append(x)

print ("I think we did it ? \n\n",mylist)



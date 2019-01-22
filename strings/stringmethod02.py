#!/usr/bin/env python3
###Alta3 research||Author:Swadipt Saurabh###

def main():
	###Run-time code###
	liststring = "Alta3 research offers classes on Python Training"
	newlist=liststring.split(" ")
	print(newlist)
	
	#create a list of strings
	myiplist = ['192','168','0','12']
	#set singleip as result of join
	singleip = ".".join(myiplist)
	#display singleip
	print (singleip)

#Call out main function
main()

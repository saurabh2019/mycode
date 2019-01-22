#!/usr/bin/env python3

##create a dictionary
switch = {'hostnmae':'sw1','ip':'10.0.1.1','version':'1.2','vendor':'cisco'}

##switch['hostname]

zinput = input ('Give me a number')

if zinput.isdigit():
	zinput = float (zinput)
else:
	print("You didn't give me a digit") 
	exit()

##postive test (return a value ==true)
switch.get('hostname')

##negative test(returns NONE ==False)
switch.get('iphone')

##Collect input from user
userinput = input('What is the key you are looking for ?')

#test that input
if switch.get(userinput) :
	print("We found a key that matches your input")
	print("The if statement is tested true")
elif userinput == "Seekrit" :
	print("You guesses the secret word")
else :
	print("we didn't find a key that matches your input")
	print("you also didn't guess secret word")

print("The program has ended.All users always see this statement")

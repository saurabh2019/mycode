#!/usr/bin/env python3
message = 'Your grade is - '
print ('Enter your score in numeric to get the grade. !!')
marks = float(input())

if marks>=90 and  marks <=100:
 message = message + ' A '
elif marks>=80 and marks <=89:
 message = message + ' B '
elif marks>=70 and marks <=79:
 message = message + ' C '
elif marks>=60 and marks <=69:
 message = message + ' D '
elif marks <=59:
 message = message + ' E '
else :
 message = message + 'F'

print ( message )


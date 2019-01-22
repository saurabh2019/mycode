#!/usr/bin/env python3
round = 0

while (True):
 round = round + 1
 print('Finish the movie title, "Monty Python\'s The Life of ______"')
 answer = input ()
 if (answer == 'Brian'):
  print('Correct')
  break
 else:
  print('Sorry! Try again!')


# First request - we want to ask how many people are working
# it will either be 2 or 3
# ask for the inputs of the names
# once we get the inputs of names we want to assign a random number from 1-3 or 1-2 based on if there is 2 or 3 people inputed
# once the number is assigned no other person can get that number until all people have been assigned a number

import random

print("How many people are working?");
working = int(input())

if working == 2:
	#random sample to get unique outputs and no duplicates
	z = random.sample(range(1, 3), 2)
	x1 = input("input name 1: ")
	x2 = input("input name 2: ")
	print(x1, " is assigned to op: ", z[0])
	print(x2, " is assigned to op: ", z[1])

else:
	#random sample to get unique instances with range of 3
	z2 = random.sample(range(1, 4), 3)
	y1 = input("input name 1: ")
	y2 = input("input name 2: ")
	y3 = input("input name 3: ")
	print(y1, " is assigned to op: ", z2[0])
	print(y2, " is assigned to op: ", z2[1])
	print(y3, " is assigned to op: ", z2[2])

print("Enjoy shift")

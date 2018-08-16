#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Somesh
#
# Created:     14/08/2018
# Copyright:   (c) Somesh 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def GCD(x, y):

	if x > y:
		small = y
	else:
		small = x
	for i in range(1, small+1):
		if((x % i == 0) and (y % i == 0)):
			gcd = i

	return gcd
x=int(input("enter the x value"))
y=int(input("enter the y value"))
z=GCD(48,60)
print ("The gcd  is : ",z)


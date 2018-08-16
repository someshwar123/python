#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Somesh
#
# Created:     12/08/2018
# Copyright:   (c) Somesh 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

array=[]
a=int(input("enter the total elements"))
for i in range(a):
    b=input("enter the array values")
    array.append(b)
print(max(array))
print(min(array))
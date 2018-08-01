#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Somesh
#
# Created:     31/07/2018
# Copyright:   (c) Somesh 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

array=[]
a= int(input("enter the no of elements"))
for i in range (0,a):
     b=int(input("enter the array value"))
     array.append(b)
     array.sort()
print("the smallest element is",array[(b-1)/2])
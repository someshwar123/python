#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Somesh
#
# Created:     12/08/2018
# Copyright:   (c) Somesh 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
array=[]
a=input("enter the total value")
count=0
for i in range(0,a):
    b=input("enter the values")
    array.append(b)
    if(array[i]==array[i]):
     count=count+1
print(count)
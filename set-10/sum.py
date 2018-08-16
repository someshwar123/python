#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Somesh
#
# Created:     15/08/2018
# Copyright:   (c) Somesh 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

array=[]
N=int(input("enter the total elements"))
sum=0
for i in range (N):
    n=int(input("enter the values"))
    array.append(n)
    sum=sum+array[i]

print(sum)

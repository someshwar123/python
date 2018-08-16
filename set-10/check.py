#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Somesh
#
# Created:     13/08/2018
# Copyright:   (c) Somesh 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

array=[]
K=int(input("enter the elements"))
count=0
N=int(input("enter the total elements"))
for i in range (N):
    n=int(input("enter the values"))
    array.append(n)
    if(array[i]==K):
       count=count+1
print(count)

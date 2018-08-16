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
a=input("enter the input elements")
tot=0
while(a>0):
    sum=a%10
    tot=tot+sum
    a=a/10
print(tot)




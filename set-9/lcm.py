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

def lcm (a,b):
    if(a>b):
       greater=a
    else:
        greater=b
    while(True):
        if((greater%a==0) and(greater%b==0)):
            lcm =greater
            break
        greater =greater+1
    return lcm

a=int(input("enter the a value"))
b=int(input("enter the b value"))
z=lcm(48,60)
print ("The lcm is : ",z)
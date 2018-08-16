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

a=raw_input("enter the string")
b=raw_input("enter the string")
count1=0
count2=0
for i in a:
    count1=count1+1
for i in b:
    count2=count2+1
if(count1>count2):
    print(a ,"is greater")
else:
    print(b ,"is greater")
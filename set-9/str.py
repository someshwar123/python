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


S=int(raw_input("enter the input value"))
sum=1
while(S>0):
 tot=S%10
 sum=sum*tot
 S=S//10
print(sum)



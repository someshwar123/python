#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      Somesh
#
# Created:     10/08/2018
# Copyright:   (c) Somesh 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

a=raw_input("enter the number value")
count=0
for i in a:
    if(a.isnumeric()):
       count=count+1
print(count)

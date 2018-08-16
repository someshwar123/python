#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Somesh
#
# Created:     10/08/2018
# Copyright:   (c) Somesh 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
a=raw_input("enter the value")
count=0
for i in a:
     if(i.isnumeric()):
       count=count+1
print(count)


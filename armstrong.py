#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      Somesh
#
# Created:     30/07/2018
# Copyright:   (c) Somesh 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

a=(int(input("enter the value")))
b=list(map(int,str(a)))
c=list(map(lambda x:x**3,b))
if(sum(c)==a):
    print("the armstrong no is ",a)

else:
    print("not a armstrong no")
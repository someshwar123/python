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
def fibonocci(n):
   if(n<=1):
       return n
   else:
      return(fibonocci(n-1) + fibonocci(n-2))
n=input("enter n value")
for i in range(n):
     print(fibonocci(i))







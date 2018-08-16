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

N=int(input("enter the input values"))
k=0
for i in range(2,N//2+1):
    if(N%i==0):
     k=k+1
if(k>1):
    print("yes")
else:
        print("no")
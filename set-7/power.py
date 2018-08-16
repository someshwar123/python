#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Somesh
#
# Created:     16/08/2018
# Copyright:   (c) Somesh 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
N=int(raw_input("enter the input value"))
A=N**2
for i in range(2,A):
    C=i**2
    if(N==C):
       d=C*2
       print(d)



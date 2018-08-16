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
print("Input the value of l ,b ,h")
L,B,H= map(int, raw_input().split())
sa = L*B*H
cu= (2*L*B + 2*B*H+ 2*H*L)
print("The value of x & y are: ",L,B,H)
print("the value of surface area  and cuboid",sa,cu)
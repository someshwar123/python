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

N=int(input("enter the input elements"))
b=list(map(int,str(N)))
c=list(map(lambda x:x%2!=0,b))
print(c)
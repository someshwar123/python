#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Somesh
#
# Created:     15/08/2018
# Copyright:   (c) Somesh 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def function(a):
   if len(a)==0:
      return(a)
   else:
    return function(a[1:])+a[0]
a=raw_input("enter the input value")
print(function(a))

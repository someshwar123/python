#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Somesh
#
# Created:     30/07/2018
# Copyright:   (c) Somesh 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

num = int(input("enter your number"))
if(num>0):
  if(num%2==0):
    print("even")
  elif(num%2!=0):
    print("odd")
elif(num<0):
  print("input is invalid")

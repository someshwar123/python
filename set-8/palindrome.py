#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Somesh
#
# Created:     13/08/2018
# Copyright:   (c) Somesh 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
a=str(raw_input("enter the string"))
str_1=reversed(a)
if list(str_1)==list(a):
    print("it is palindrome")
else:
    print("it is not palindrome")


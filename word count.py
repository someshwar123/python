#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Somesh
#
# Created:     10/08/2018
# Copyright:   (c) Somesh 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

a=raw_input("enter the string")
char=0
word=1
for i in a:

    if(i==' '):
        word=word+1
print(word)

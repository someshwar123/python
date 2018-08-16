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

str=raw_input("enter the string value")

word=1
for i in str:

    if(i=='.'):
        word=word+1
print(word)

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

def isogram(word):
     mword=word.lower()
     letterlist=[]
     for i in mword:
        if letter.isalpha():
            if i in letterlist:
                return False
            letterlist.append(i)
     return True


isogram(word)
word=raw_input("enter the input value")

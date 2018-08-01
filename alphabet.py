#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Somesh
#
# Created:     30/07/2018
# Copyright:   (c) Somesh 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

a = input('Enter a word:')
b = a.lower()
first = b[0]

if len(a) > 0 and a.isalpha():
    if first in 'aeiou':
        print "vowel"
    else:
        print "consonant"
else:
    print "invalid"

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

original = raw_input('Enter a word:')
word = original.lower()
first = word[0]

if len(original) > 0 and original.isalpha():
    if first in 'aeiou':
        print "vowel"
    else:
        print "consonant"
else:
    print "invalid"


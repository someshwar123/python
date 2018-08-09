#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      Somesh
#
# Created:     01/08/2018
# Copyright:   (c) Somesh 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

array = []
n = int(raw_input('Enter how many elements you want: '))
for i in range(0, n):
    x = raw_input('Enter the numbers into the array: ')
    array.append(x)

    print(array[i],i)


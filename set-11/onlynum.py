#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Somesh
#
# Created:     16/08/2018
# Copyright:   (c) Somesh 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import re
a=(raw_input("enter the elements "))
B=a.lower()
B=re.sub('[a-z]','',B)
print(B)






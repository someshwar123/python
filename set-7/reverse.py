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

startmsg="hello"
endmsg=""
for i in range(0,len(startmsg)):
    endmsg=startmsg[i]+endmsg
    print(endmsg)
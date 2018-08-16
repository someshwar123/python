#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Somesh
#
# Created:     15/08/2018
# Copyright:   (c) Somesh 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

S,N=map(int,raw_input().split())

for i in range(N):
      A=S%10
      S=S//10

      print(A)


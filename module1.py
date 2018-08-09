#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Somesh
#
# Created:     08/08/2018
# Copyright:   (c) Somesh 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pymysql
conn = pymysql.connect(host="localhost",user="root",passwd="",db="mypython")
Mycursor=conn.cursor()
mycursor.execute("INSERT INTO names (id,name) VALUES(1,'somesh');")
print(">DATA INSERTED!!")

conn.commit()
conn.close()





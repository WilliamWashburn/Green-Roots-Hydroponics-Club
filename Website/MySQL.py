#https://mysqlclient.readthedocs.io/user_guide.html#connection-objects
#https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/
#https://pythonhosted.org/pyserial/shortintro.html#readline

import time
import sys
import MySQLdb as mariadb

#this connects to the database
con = mariadb.connect(host='10.104.168.255',user='test',passwd='greenroots',db='greenrootsdb');

cursor = con.cursor()

try:
	while 1:

		insert_stmt = (
			"INSERT INTO RoomSetup (Weight, Temperature)"
			"VALUES (%s, %s)"
		)
		data = (1, 2)

		cursor.execute(insert_stmt,data)
		con.commit()

		time.sleep ( 1 );

except KeyboardInterrupt:
	con.close()
	ser.close()

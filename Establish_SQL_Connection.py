import mysql.connector


con =  mysql.connector.connect(user = 'root',password = 'root', host = '127.0.0.1',database = 'Nasa')
cursor = con.cursor()
cursor.execute("Select * from state_data")
data = cursor.fetchall ()
# print the rows
for row in data :
    print row[0], row[1]
con.close()

# cursor.execute("select version()")
# data = cursor.fetchone()
# print "data base version is : " , data
# con.close()

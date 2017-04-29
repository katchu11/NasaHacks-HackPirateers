import mysql.connector

#Put the user, password , the host IPv4 and the database name
con =  mysql.connector.connect(user = 'root',password = 'root', host = '127.0.0.1',database = 'Nasa')
#Create cursor to execute commands
cursor = con.cursor()
#SQL Query
cursor.execute("Select * from state_data")
#Fetch All Rows
data = cursor.fetchall ()
# print the rows
for row in data :
    print row[0], row[1]
con.close()

# cursor.execute("select version()")
# data = cursor.fetchone()
# print "data base version is : " , data
# con.close()

'''
Created on Apr 29, 2017

@author: KrishnanRam
'''

from __future__ import division
from numpy import real
import pymysql
# from pyspark import SparkConf, SparkContext
# from pyspark.sql import SQLContext

#from mysqlx.connection import catch_network_exception



connection = pymysql.Connect(host='localhost',user='root',password='MyNewPass',db='mysql',charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()
#query = "LOAD DATA INFILE '/tmp/myfile1.txt ' INTO TABLE wolfram FIELDS TERMINATED BY '|' ENCLOSED BY '' ESCAPED BY '\n'"

#Names are Variable



cursor.execute("SELECT gender FROM entries")
result = cursor.fetchone()
gender = result.values()[0]
connection.commit()
print gender
cursor.execute("SELECT ethnicity FROM entries")
result = cursor.fetchone()
race = result.values()[0]
connection.commit()
print race
cursor.execute("SELECT location FROM entries")
result = cursor.fetchone()
location = result.values()[0]
connection.commit()
print location




query = "SELECT pop_est_2014 FROM census_state_populations WHERE state = '%s' "  % (location)



x = 0
#This gets population in state
cursor.execute( query )
result = cursor.fetchone()
print result
print result.values()
x = result.values()[0]
connection.commit()
#print x

y = ""
#This gets percentage of race in state
query = "SELECT %s FROM ethnic WHERE location = '%s'  "  % (race,location)
cursor.execute( query )
result = cursor.fetchone()
y = result.values()[0]
y = float(y)
connection.commit()
#Print amount of race in state
f = x * y 
print f


z = ""
#Percent of acute conjunctivitis for gender and race 
query = "SELECT %s FROM wolfram_acute WHERE circumstance = '%s' "  % (gender,race)
cursor.execute( query )
result = cursor.fetchone()
z = result.values()[0]
#Prevent error when string gives ~~0
try:
    z = float(z)
    z = z/100
except:
    z = 0
    z=z/100
connection.commit()

g = z * f
print g  


recovered = (1/7)*(g/x)
#recovered = round(recovered)
print recovered
susc = (1/25) * (x/x) * (g)
#susc = round(susc)
print susc
infected = susc - recovered
print infected
#Number_of_ppl_who_are_infected
disease = "Acute Conjunctivitis"
#percent_rate = (g/d)/100
#res = str(infected)
#res = round(res,2)
#print Infected_Formula(x, g)
print "Value: ",infected

location = location.replace(" ", "")
print location
print race,gender,g
circum = location + race + gender 
print circum
#infect = str(infected)
# query = "INSERT INTO end_res(circumstance, pop) VALUES(%s ,%s)" , (circum, str(g) )
cursor.execute("INSERT INTO end_res(location,race,gender, pop, infectedpop) VALUES (%s, %s, %s, %s, %s)" , (location, race,gender, str(g), str(infected)))
connection.commit()








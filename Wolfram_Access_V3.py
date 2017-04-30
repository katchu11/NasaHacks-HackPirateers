'''
Created on Apr 29, 2017

@author: Kashyap
'''
'''
Created on Apr 29, 2017

@author: KrishnanRam
'''
import wolframalpha
#import pandas
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
import pymysql


#from pyspark.shell import sqlContext
import sys
from random import randint
 
# The 'os' library allows us to read the environment variable SPARK_HOME defined in the IDE environment
import os
import re
 
# Configure the Spark context to give a name to the application
# sparkConf = SparkConf().setAppName("test")
# conf = SparkConf()
# sc = SparkContext(conf = conf)
# sqlContext = SQLContext(sc)
                        
input = raw_input("Question: ")
app_id = "T4GTHA-JV3YETWVAV"
client = wolframalpha.Client(app_id)
  
res = client.query(input)
#y = '"'
  
  
#arr = ""
  
  
#df = res.pods.toDataFrame()
#print res.pod(1)
#arr1 = [0,1,2,3,4,5,6]
# dataframe_mysql = sqlContext.read.format("jdbc").options(
#     url="jdbc:mysql://localhost:3306/mysql",
#     driver = "com.mysql.jdbc.Driver",
#     dbtable = "neighbors_states",
#     user="root",
#     password="MyNewPass").load()
      
x = 3
  
for pod in res.pods :
      
       
     if pod.title == "Patients with diagnosis in a given year":
         f = open('test' + str(x) + '.txt', 'w')
         print pod.title
           
          
         f.write(pod.text + '\n') 
         f.close() 
         x += 1
         print x
     elif pod.title == "Annual diagnosis rates in patient subpopulations":
         f = open('Annual_Diagnosis_rates' + str(x) + '.txt', 'w')
         print pod.title
           
          
         f.write(pod.text + '\n') 
         f.close() 
         x += 1
         print x
          
    #dataframe_mysql.show()
    
    #dataframe_mysql.registerTempTable("wolfram" + x)
# y = '"'
# # dataframe_mysql.registerTempTable("neighbors_states")
# # sqlContext.sql("select * from neighbors_states").show(200)
# sqlContext.sql("LOAD DATA LOCAL INFILE '/Users/KrishnanRam/Documents/workspace/MyPythonSparkProject/src/myfile1' INTO TABLE wolfram FIELDS TERMINATED BY '|' ENCLOSED BY '" + y + "' LINES TERMINATED BY '\n' IGNORE 1 LINES")



#Fix this error

# connection = pymysql.Connect(host='localhost',user='root',password='root',db='nasa',charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
# cursor = connection.cursor()
# query = "LOAD DATA INFILE 'C:\Users\Kashyap\workspace\NasaHacks\Annual_Diagnosis_rates4.txt' INTO TABLE wolfram FIELDS TERMINATED BY '|' ENCLOSED BY '' ESCAPED BY '\n'"
# query1 = "LOAD DATA INFILE 'C:\Users\Kashyap\workspace\NasaHacks\test3.txt' INTO TABLE wolfram1 FIELDS TERMINATED BY '|' ENCLOSED BY '' ESCAPED BY '\n'"
# cursor.execute( query )
# cursor.execute(query1)
# connection.commit()
# connection.close()
    #dataframe_mysql.registerTable = "wolfram" + x
     
     
    






#df = pod1.toDataFrame()
#df = arr.toDataFrame()
#print df
#answer = next(res.results)
#pd.DataFrame.from_dict(answer)
#df =  pd.DataFrame(answer)
#print list(df.columns.values)
#print df
#print list(df.loc['state']['states'])
#print df
#file_object = open("test23.txt","w")
#print file_object
#file_object.write(repr(answer))
#print file_object
#file_object.close()
#print answer

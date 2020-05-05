#!/usr/bin/env python
# coding: utf-8

# In[25]:


import psycopg2          # for PostgreSQL
import mysql.connector   #for Mysql server 
import pyodbc            # for Sql server 


# In[26]:


#get the database data 
database = input('What database you use ? PostgreSQL,Mysql  or Sql Server ?: ')


# In[27]:


#lets define one function for each database authentication and connection 
def mysql(hostname, username , password ) :
    
    connection = mysql.connector.connect(host = hostname , user = username , passwd = password ) 
    cursor = connection.cursor()
    
def Postgre(username , password, host, port , databasename):
    
    connection = psycopg2.connect(  username=username , password=password , host=host, port=port , database=databasename)
    cursor = connection.cursor()

def SqlServer(driver, server , database):
    
    connection = pyodbc.connect(driver = driver, host = server , database = database  )
    cursor = connection.cursor()


# In[28]:


database = database.upper() # make it all UPPER 

#if statement for database type 
if database== 'MYSQL' : 
    #get the characteristics : 
    hostname = input('Give Hostname :')
    username = input('Gine username :')
    password = input('Give password :')
    #run function 
    mysql(hostname, username , password )
    
elif database == 'SQLSERVER':
        
    driver = input('Give driver :')
    server =input('Give server  :')
    database = input('Give database name  :')
    
    SqlServer(driver, server , database)
    
elif database == 'POSTGRESQL' :
        
    username = input('Give username :')
    password = input('Give password :')
    host     = input('Give host ip : ')
    port     = input('Give port :')
    databasename = input('Give database name : ')
    
    Postgre(username , password, host, port , databasename)


# In[21]:





# In[22]:


#lets see a query : 


# In[29]:


cursor.execute('SELECT TOP 5 * FROM dbo.nari_dynamic_dec ')


# In[30]:


for row in cursor:
    print(row)


# In[ ]:





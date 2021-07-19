#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install mysql-connector-python')


# In[2]:


import mysql.connector as connection


# In[3]:


mydb=connection.connect(host="localhost",user="root",password="rahulinsan15@")


# In[4]:


query="SHOW DATABASES"
cursor=mydb.cursor()
cursor.execute(query)
cursor.fetchall()


# In[6]:


import mysql.connector as connection
try:
    mydb=connection.connect(host="localhost",user="root",password="rahulinsan15@")
    print(mydb.is_connected())
    
    query="create database student;"
    cursor=mydb.cursor()
    cursor.execute(query)
    print("Database created")
    mydb.close()
except Exception as e:
    mydb.close()
    print(str(e))
    


# In[8]:


mydb=connection.connect(host="localhost",user="root",password="rahulinsan15@")
query="show databases"
cursor=mydb.cursor()
cursor.execute(query)
cursor.fetchall()


# In[14]:


import mysql.connector as connection
try:
    rahul=connection.connect(host="localhost",database="student",user="root",password="rahulinsan15@")
    print(rahul.is_connected())
    query="CREATE TABLE studentdetails(RollNO int(10) AUTO_INCREMENT PRIMARY KEY,First_Name VARCHAR(60),"           "Last_Name VARCHAR(60),DOB Date,section VARCHAR(5))"
    yadav=rahul.cursor()
    yadav.execute(query)
    print("table created!")
    rahul.close()
except Exception as e:
    rahul.close()
    print(str(e))


# In[20]:


import mysql.connector as connection
try:
    mydb=connection.connect(host="localhost",database="student",user="root",password="rahulinsan15@")
    print(mydb.is_connected())
    query="Insert into studentdetails values('1','Amit','kumar','1994-10-09','D');"
    cursor=mydb.cursor()
    cursor.execute(query)
    print("values inserted")
    mydb.commit()
    mydb.close()
except Exception as e:
    mydb.close()
    print(str(e))


# In[26]:


import mysql.connector as connection 
try:
    mydb=connection.connect(host="localhost",database="student",user="root",password="rahulinsan15@")
    print(mydb.is_connected())
    query="insert into studentdetails values('3','Annu','verma','1994-10-02','A')"
    cursor=mydb.cursor()
    cursor.execute(query)
    cursor.execute("insert into studentdetails values('4','Aamir','khan','1995-11-9','C')")
    cursor.execute("insert into studentdetails values('5','Bala','singh','1993-03-25','C')")
    cursor.execute("insert into studentdetails values('6','chetan','agnihotri','1996-11-19','D')")
    print("values inserted")
    mydb.commit()
    mydb.close()
except Exception as e:
    mydb.close()
    print(str(e))


# In[30]:


import mysql.connector as connection
mydb=connection.connect(host="localhost",user="root",password="rahulinsan15@")
print(mydb.is_connected())
query="select * from student.studentdetails;"
cursor=mydb.cursor()
cursor.execute(query)
cursor.fetchall()
    


# In[33]:


import csv


# In[31]:


mydb=connection.connect(host="localhost",user="root",password="rahulinsan15@")


# In[54]:


cur=mydb.cursor()
cur.execute("CREATE TABLE student.store1(Item_Identifier varchar(30),Item_Weight float,Item_Fat_Content varchar(40),Item_Visibility float,Item_Type varchar(40),Item_MRP float,Outlet_Identifier varchar(50),Outlet_Establishment_Year int(15),Outlet_Size varchar(30),Outlet_Location_Type varchar(30),Outlet_Type varchar(30))")


# In[55]:


with open("F:\Test.csv","r") as rah:
    next(rah)
    data_csv=csv.reader(rah)
    for i in enumerate(data_csv):
        print(i)
        for j in i[1]:
            cur.execute('insert into student.store1 values({data})'.format(data=(j)))
    print("all data inserted")
mydb.commit()


# In[ ]:





# In[ ]:





# In[ ]:





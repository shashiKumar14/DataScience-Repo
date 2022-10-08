import mysql.connector as conn
import os
from dotenv import load_dotenv

load_dotenv()
host=os.environ['host']
user=os.environ['user']
passwd=os.environ['passwd']

mydb=conn.connect(host=host,user=user,passwd=passwd)
print(mydb)

cursor=mydb.cursor()
# cursor.execute("create database shashineuron")
# cursor.execute("show databases")
# s="create table shashineuron.shashidetails1(employee_id int(10),emp_name varchar(80) ,emp_mail_id varchar(20) ,emp_salary int(6) ,emp_att int(3) ) "
# q1=cursor.execute(s)
# print(cursor.fetchall())
s2="select * from shashineuron.shashidetails1"
cursor.execute(s2)




import mysql.connector as conn
import os
from dotenv import load_dotenv

load_dotenv()
host=os.environ['host']
user=os.environ['user']
passwd=os.environ['passwd']

mydb=conn.connect(host=host,user=user,passwd=passwd)
cursor=mydb.cursor()

cursor.execute("select employee_id,emp_name from shashineuron.shashidetails1")

l=[]

for i in cursor.fetchall():
    l.append(i)
print(l)

print(type(l[0]))
import mysql.connector as conn
import os
from dotenv import load_dotenv

load_dotenv()
host=os.environ['host']
user=os.environ['user']
passwd=os.environ['passwd']

mydb=conn.connect(host=host,user=user,passwd=passwd)
cursor=mydb.cursor()

cursor.execute(" insert into shashineuron.shashidetails1 values(101,'shashi','mail',1222222,232)")
cursor.execute(" insert into shashineuron.shashidetails1 values(101,'shashi','mail',1222222,232)")

mydb.commit()
cursor.execute("select * from shashineuron.shashidetails1")
for i in  cursor.fetchall():
    print(i)

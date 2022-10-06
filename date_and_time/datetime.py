import datetime
import time

#Today date below format
Todaydate = datetime.datetime.now().strftime("%Y-%m-%d-%I:%M:%S_%p") #2022-09-22 17:05:20

#How much time taken to process
start=time.time()#starting of code
end=time.time()#ending of the code
print(end-start)

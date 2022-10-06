import shedule

schedule.every(10).seconds.do(calling_the_function_for_code)#run the code every 10 seconds
while 1:
    schedule.run_pending()
    time.sleep(1)

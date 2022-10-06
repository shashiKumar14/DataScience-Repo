import logging

#The output will get with time and text
logging.basicConfig(filename="test.log",level=logging.INFO,format='%(asctime)s %(message)s')

or

#The output will get with only text
logging.basicConfig(filename="test.log",level=logging.INFO,format='%(message)s')


logging.info(f"In place of print we write this")

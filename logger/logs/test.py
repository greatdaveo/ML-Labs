from logger import logging

def add(a, b):
    logging.debug("The additional operation is taking place")
    return a + b

logging.debug("The additional function is called")
add(10, 15)

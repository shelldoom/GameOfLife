import logging

logging.basicConfig(
    filename='debug.log', 
    filemode='a',
    level=logging.DEBUG,
    format='%(levelname)s - %(asctime)s - %(message)s'
)
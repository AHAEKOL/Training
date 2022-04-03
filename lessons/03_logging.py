import logging

# logger definition
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)

# logging example
logging.info('Program started...')
for x in range(15):
    logging.info('The value is: ' + str(x))
logging.error('Something bad happened')



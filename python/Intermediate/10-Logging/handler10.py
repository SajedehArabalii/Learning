import logging
logger = logging.getLogger(__name__)

#Create handler
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

#level and the format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

#Specify foramatter
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

#Add handler to logger
logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('This is a warning')
logger.error('This is an error')
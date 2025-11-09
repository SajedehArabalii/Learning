"""
I have to come back to this, the Rotating File Handler and Timed Rotatig File Handler are not working as expected

review:
    RotatingFileHandler
    TimedRotatingFileHandler
"""
#Logging in Python is a built-in mechanism provided by the logging module that allows developers to track events, record messages, and monitor the execution of their programs. It is especially useful for debugging, diagnosing issues, and understanding the flow of an application

#Five levels of logging
#only the messages with high levels are printed
import logging 

# Clear existing handlers
# By default, the root logger only outputs messages at level WARNING or higher. So even though you’ve set level=logging.DEBUG in basicConfig, if any logging configuration was already set earlier (even by an imported module), basicConfig will have no effect
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

# Now configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S'
)
#Test messages
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

#Named logger
import helper10

#A handler object in Python’s logging module is like a delivery system for your log messages. It decides where the logs go — to the console, a file, an email, a network socket, etc.
import logging.config
import sys  # Required for sys.stdout in config
logging.config.fileConfig('logging10.conf')
logger = logging.getLogger('simpleExample')
logger.debug('This is the debug message')


#Capturing stack traces: ecording the sequence of function calls that led to a specific point in your program — usually when an error or exception occurs.
"""
A stack trace shows:

The file name

The line number

The function name

The exact line of code
"""
try:
    a = [1,2,3]
    val = a[4]
except IndexError as e:
    logging.error(e)
    
    
#If we don't know the type of Error and with more info
import traceback
try:
    a = [1,2,3]
    val = a[4]
except:
    logging.error("The error is %s", traceback.format_exc())
    
#Rotating file handler:a special type of handler that writes log messages to a file — and automatically creates a new file when the current one gets too big.

from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create handler
handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)

# Add a formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add handler to logger
logger.addHandler(handler)

# Log messages
for _ in range(10000):
    logger.info("Hello, World")

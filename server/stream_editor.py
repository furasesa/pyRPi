import RPi.GPIO as GPIO
from controller import Config

# import logging

# logging.basicConfig(filename='debug.log',level=logging.DEBUG)
# logging.debug('This message should go to the log file')
# logging.info('So should this')
# logging.warning('And this, too')


c = Config()

GPIO.setmode(c.get_mode)
ch_in = c.get_ch_in
ch_out = c.get_ch_out

GPIO.setup(ch_in,GPIO.IN)
GPIO.setup(ch_out,GPIO.OUT)


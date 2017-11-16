version = '0.0.1'

    

'''
TODO : make

example:
rpi.py config
rpi.py tcp
rpi.py firebase

-----service-----
arguments :
+S enable service
-S disable service

example:
rpi +S tcp -p[--port] 2303
rpi -S tcp

---- config ------
config editor
rpi -c channel setup 0

example:
change channel 17 to GPIO.IN
rpi -c 17 -s 0
rpi -c 17 -s GPIO.IN

change channel 17 to GPIO.OUT
rpi -c 17 -s 1

'''

import argparse
parser = argparse.ArgumentParser(description='raspberry GPIO config editor',
prefix_chars='-+')

# Serive

# parser.add_argument('-S', '--service',
#     action="store_false", 
#     default=None,
#     help='print GPIO config')

# parser.add_argument('+S', '++service',
#     action="store_true", 
#     default=None,
#     help='print GPIO config')

parser.add_argument('service_name',
    help='Config, TCP, firebase')

# parser.add_argument('-p', '--port',
#     type = int,
#     action="store",
#     dest = 'tcp_port', 
#     default=2303,
#     help='TCP port')

#Config editor
# parser.add_argument('-c', '--channel',
#     type = int,
#     action="store",
#     dest = 'channel', 
#     help='GPIO channel')

# parser.add_argument('-s', '--setup',
#     type = int,
#     action="store",
#     dest = 'IO', 
#     help='GPIO.IN (0),  GPIO.OUT(1)')

arg = parser.parse_args()

if arg.service_name == 'config':
    from config import Config
    print('config')
    c = Config()
    
elif arg.service_name == 'tcp':
    print('enable tcp service')

# if r.service:
#     if r.service_name == 'tcp':
#         print ('enable TCP at port',r.tcp_port)
#     elif r.service_name == 'firebase':
#         print('firebase')
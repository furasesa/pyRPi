'''
RPi.GPIO testing
'''

BCM = 11
BOARD = 10
IN = 1
OUT = 0
LOW = 0
HIGH = 1
PWM = 'PWM Class'

channel_in = []
channel_out = []
channel = []

def setmode(MODE):
    global selectedmode
    selectedmode = MODE

def getmode():
    if selectedmode == BCM:
        print('mode = BCM')
    else:
        print ('mode = BOARD')

def setwarnings (flag):
    global warninglevel
    warninglevel=flag

def setup(channel, MODE):
    global ci
    global co
    
    if MODE == IN:
        if type(channel) is int:
            ci = channel_in.append(channel)
        elif type(channel) is list:
            ci = channel
        # print ('channel INPUT mode',channel_in)
    elif MODE == OUT:
        if type(channel) is int:
            co = channel_out.append(channel)
        elif type(channel) is list:
            co = channel
        # print ('channel OUTPUT mode',channel_out)
    else :
        print('fuck?')

def list_ci():
    print ('GPIO.IN :',ci)
def list_co():
    print ('GPIO.OUT :',co)

def input(channel): #read input
    print('read input at channel :',channel,'=>','0 off or 1 on')

def output(channel,state) : 
    for i in co:
        if i == channel :
            print ('channel',channel,'change to state',state)

    
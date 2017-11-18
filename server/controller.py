version = '0.0.2'
db_version = '0.0.2'
import json
import lib.hwid as hwid
import RPi.GPIO as GPIO
from lib.dict import Dictionary

'''
PWM still not tested
'''

def build_config():
    config = {
            hwid.get_uuid() : {
                "config" : {
                    "alias" : "kacung",
                    "mode" : 11,
                    "version" : db_version
                },

                "channel" : {
                    17 : {
                        "name" : "GPIO_GEN0",
                        "setup" : GPIO.IN,
                        "voltage" : GPIO.LOW,
                        "PWM" : False,
                        "freq" : 1,
                        "dc" : 100
                    },
                    18 : {
                        "name" : "GPIO_GEN1",
                        "setup" : GPIO.IN,
                        "voltage" : GPIO.LOW,
                        "PWM" : False,
                        "freq" : 1,
                        "dc" : 100
                    },
                    27 : {
                        "name" : "GPIO_GEN2",
                        "setup" : GPIO.IN,
                        "voltage" : GPIO.LOW,
                        "PWM" : False,
                        "freq" : 1,
                        "dc" : 100
                    },
                    22 : {
                        "name" : "GPIO_GEN3",
                        "setup" : GPIO.IN,
                        "voltage" : GPIO.LOW,
                        "PWM" : False,
                        "freq" : 1,
                        "dc" : 100
                    },
                    23 : {
                        "name" : "GPIO_GEN4",
                        "setup" : GPIO.IN,
                        "voltage" : GPIO.LOW,
                        "PWM" : False,
                        "freq" : 1,
                        "dc" : 100
                    },
                    24 : {
                        "name" : "GPIO_GEN5",
                        "setup" : GPIO.IN,
                        "voltage" : GPIO.LOW,
                        "PWM" : False,
                        "freq" : 1,
                        "dc" : 100
                    },
                    25 : {
                        "name" : "GPIO_GEN6",
                        "setup" : GPIO.IN,
                        "voltage" : GPIO.LOW,
                        "PWM" : False,
                        "freq" : 1,
                        "dc" : 100
                    }
                }
            }
        }
    
    with open('gpio_conf.json', 'w') as f:
        json.dump(config, f)

class Config:
    def __init__(self):
        try:
            with open ('gpio_conf.json','r') as f:
                conf = json.load(f)
        except FileNotFoundError as ex:
            print (ex)
            build_config()
            # try load again
            with open ('gpio_conf.json','r') as f:
                conf = json.load(f)
        d = Dictionary(conf)
        print ('=========== Reading Config ===========')
        self.uuid = hwid.get_uuid()
        self.alias =  d[self.uuid]['config']['alias']
        self.mode = d[self.uuid]['config']['mode']
        self.db_v = d[self.uuid]['config']['version']
        print ('alias :',self.alias,'\nmode :',self.mode,'\nversion :',self.db_v)
        print ('========== Reading Channel Setup ===========')
        self.ch_in = []
        self.ch_out = []

        get_ch = d[self.uuid]['channel']
        for ch in get_ch:
            get_setup = d[self.uuid]['channel'][ch]['setup']
            if get_setup == GPIO.IN:
                print('channel',ch,'is GPIO.IN')
                self.ch_in.append(ch)
            elif get_setup == GPIO.OUT:
                print('channel',ch,'is GPIO.OUT')
                self.ch_out.append(ch)
            if ch == '17':
                self.ch17_voltage =  d[self.uuid]['channel'][ch]['voltage']
                self.ch17_pwm = d[self.uuid]['channel'][ch]['PWM']
                self.ch17_freq = d[self.uuid]['channel'][ch]['freq']
                self.ch17_dc = d[self.uuid]['channel'][ch]['dc']
                print('channel 17 setting :',self.ch17_voltage,self.ch17_pwm,self.ch17_freq,self.ch17_dc)
            elif ch == '18':
                self.ch18_voltage =  d[self.uuid]['channel'][ch]['voltage']
                self.ch18_pwm = d[self.uuid]['channel'][ch]['PWM']
                self.ch18_freq = d[self.uuid]['channel'][ch]['freq']
                self.ch18_dc = d[self.uuid]['channel'][ch]['dc']
            elif ch == '27':
                self.ch27_voltage =  d[self.uuid]['channel'][ch]['voltage']
                self.ch27_pwm = d[self.uuid]['channel'][ch]['PWM']
                self.ch27_freq = d[self.uuid]['channel'][ch]['freq']
                self.ch27_dc = d[self.uuid]['channel'][ch]['dc']
            elif ch == '22':
                self.ch22_voltage =  d[self.uuid]['channel'][ch]['voltage']
                self.ch22_pwm = d[self.uuid]['channel'][ch]['PWM']
                self.ch22_freq = d[self.uuid]['channel'][ch]['freq']
                self.ch22_dc = d[self.uuid]['channel'][ch]['dc']
            elif ch == '23':
                self.ch23_voltage =  d[self.uuid]['channel'][ch]['voltage']
                self.ch23_pwm = d[self.uuid]['channel'][ch]['PWM']
                self.ch23_freq = d[self.uuid]['channel'][ch]['freq']
                self.ch23_dc = d[self.uuid]['channel'][ch]['dc']
            elif ch == '24':
                self.ch24_voltage =  d[self.uuid]['channel'][ch]['voltage']
                self.ch24_pwm = d[self.uuid]['channel'][ch]['PWM']
                self.ch24_freq = d[self.uuid]['channel'][ch]['freq']
                self.ch24_dc = d[self.uuid]['channel'][ch]['dc']
            elif ch == '25':
                self.ch25_voltage =  d[self.uuid]['channel'][ch]['voltage']
                self.ch25_pwm = d[self.uuid]['channel'][ch]['PWM']
                self.ch25_freq = d[self.uuid]['channel'][ch]['freq']
                self.ch25_dc = d[self.uuid]['channel'][ch]['dc']
        print ('========== Setup Report ===========')
        print('list of GPIO.IN :',self.ch_in)
        print('list of GPIO.OUT :',self.ch_out)
        # print('uuid :',self.uuid,'\nmode :',self.mode,'\nchannel(Input) :',self.ch_in,'\nchanne(output) :',self.ch_out)

    # alias setter
    def set_alias (self,alias_name):
        self.alias = alias_name
    # mode setter
    def set_mode (self, mode):
        self.mode = mode
    
    def setup(self, channel, value): #complete
        print (channel, 'change to', value)
        if type(channel) is str:
            print('channel type is int')
            if value == GPIO.IN:
                try:
                    self.ch_out.remove(channel)
                except Exception:
                    pass
                self.ch_in.append(channel)
            elif value == GPIO.OUT:
                try:
                    self.ch_in.remove(channel)
                except Exception:
                    pass
                self.ch_out.append(channel)
            else:
                print("setup => I Dont know")
        elif type(channel) is list:
            if value == GPIO.IN:
                # finding collision for each in GPIO.OUT
                for my_wish_ch in channel:
                    try:
                        self.ch_out.remove(my_wish_ch)
                        # success remove
                        self.ch_in.append(my_wish_ch)
                    except Exception as ex:
                        print (ex)
            elif value == GPIO.OUT:
                # finding collision for each in GPIO.IN
                for my_wish_ch in channel:
                    try:
                        self.ch_in.remove(my_wish_ch)
                        # success remove
                        self.ch_out.append(my_wish_ch)
                    except Exception as ex:
                        print (ex)
                print('I dont know')

        print ('GPIO.IN list :',self.ch_in)
        print ('GPIO.OUT list :',self.ch_out)
        
    def output(self, channel, value):
        if type(value)is not int:
            print('value must be int type')
            pass
        if type(channel) is str:
            for i in self.ch_out:
                if i == channel:
                    print('channel',channel,'is GPIO.OUT')
                    if i =='17':
                        print('channel 17 voltage to',value)
                        self.ch17_voltage = value
                    elif i == '18':
                        self.ch18_voltage = value
                    elif i == '27':
                        self.ch27_voltage = value
                    elif i == '22':
                        self.ch22_voltage = value
                    elif i == '23':
                        self.ch23_voltage = value
                    elif i == '24':
                        self.ch24_voltage = value
                    elif i == '25':
                        self.ch25_voltage = value
                    else :
                        pass

                else :
                    print('channel',channel,'is not GPIO.OUT')
                    pass

    def save (self):
        # generating current setup

        # for cur_ch in self.ch_in:
            # print ('cuurent channel :',selcur_ch)
        for cur_ch_in in self.ch_in:
            if cur_ch_in == '17':
                ch17_setup = GPIO.IN
            elif cur_ch_in == '18':
                ch18_setup = GPIO.IN
            elif cur_ch_in == '27':
                ch27_setup = GPIO.IN
            elif cur_ch_in == '22':
                ch22_setup = GPIO.IN
            elif cur_ch_in == '23':
                ch23_setup = GPIO.IN
            elif cur_ch_in == '24':
                ch24_setup = GPIO.IN
            elif cur_ch_in == '25':
                ch25_setup = GPIO.IN
        
        for cur_ch_out in self.ch_out:
            if cur_ch_out == '17':
                ch17_setup = GPIO.OUT
            elif cur_ch_out == '18':
                ch18_setup = GPIO.OUT
            elif cur_ch_out == '27':
                ch27_setup = GPIO.OUT
            elif cur_ch_out == '22':
                ch22_setup = GPIO.OUT
            elif cur_ch_out == '23':
                ch23_setup = GPIO.OUT
            elif cur_ch_out == '24':
                ch24_setup = GPIO.OUT
            elif cur_ch_out == '25':
                ch25_setup = GPIO.OUT
        
        cur_config = {
            hwid.get_uuid() : {
                "config" : {
                    "alias" : self.alias,
                    "mode" : self.mode,
                    "version" : db_version
                },

                "channel" : {
                    17 : {
                        "name" : "GPIO_GEN0",
                        "setup" : ch17_setup,
                        "voltage" : self.ch17_voltage,
                        "PWM" : self.ch17_pwm,
                        "freq" : 1,
                        "dc" : 100
                    },
                    18 : {
                        "name" : "GPIO_GEN1",
                        "setup" : ch18_setup,
                        "voltage" : self.ch18_voltage,
                        "PWM" : self.ch18_pwm,
                        "freq" : 1,
                        "dc" : 100
                    },
                    27 : {
                        "name" : "GPIO_GEN2",
                        "setup" : ch27_setup,
                        "voltage" : self.ch27_voltage,
                        "PWM" : self.ch27_pwm,
                        "freq" : 1,
                        "dc" : 100
                    },
                    22 : {
                        "name" : "GPIO_GEN3",
                        "setup" : ch22_setup,
                        "voltage" : self.ch22_voltage,
                        "PWM" : self.ch22_pwm,
                        "freq" : 1,
                        "dc" : 100
                    },
                    23 : {
                        "name" : "GPIO_GEN4",
                        "setup" : ch23_setup,
                        "voltage" : self.ch23_voltage,
                        "PWM" : self.ch23_pwm,
                        "freq" : 1,
                        "dc" : 100
                    },
                    24 : {
                        "name" : "GPIO_GEN5",
                        "setup" : ch24_setup,
                        "voltage" : self.ch24_voltage,
                        "PWM" : self.ch24_pwm,
                        "freq" : 1,
                        "dc" : 100
                    },
                    25 : {
                        "name" : "GPIO_GEN6",
                        "setup" : ch25_setup,
                        "voltage" : self.ch25_voltage,
                        "PWM" : self.ch25_pwm,
                        "freq" : 1,
                        "dc" : 100
                    }
                }
            }
        }
    
        with open('gpio_conf.json', 'w') as f:
            json.dump(cur_config, f)

if __name__ == '__main__':
    '''
    call Class Config
    c = Config()

    # tested setup
    ch_out = ['17','18','27','22','23','24']
    c.setup(ch_out,GPIO.OUT)
    ch_in = ['22','23','24','25']
    c.setup(ch_in,GPIO.IN)

    c.setup('17',GPIO.IN)
    c.setup('25',GPIO.OUT)

    #


    '''
    c = Config()
    
    # ch_in = ['17','18','27','22','23','24']
    # c.setup(ch_in,GPIO.IN)
    # c.setup('17',GPIO.OUT)
    # c.setup('25', GPIO.IN)
    # c.save()

    # c.output('18',1)
    # c.save()
    

    # c.setup('18',GPIO.OUT)
    # c.setup(ch_in,GPIO.IN)
    # c.setup('22', GPIO.OUT)
    # mch_in = [27,22,23,24,25]
    # mch_out = [17,18,]
    # c.Setup(mch_in,GPIO.IN)
    # c.Setup(mch_out,GPIO.OUT)
    # c.init_config()
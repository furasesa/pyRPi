version = '0.0.1'
import json
import lib.hwid as hwid
import RPi.GPIO as GPIO
from lib.dict import Dictionary



class Config:
    def __init__(self):
        with open ('config.json','r') as f:
            conf = json.load(f)
        d = Dictionary(conf)
        self.uuid = hwid.get_uuid()
        self.mode = d[self.uuid]['config']['mode']
        self.ch_in = d[self.uuid]['config']['ch_in']
        self.ch_out = d[self.uuid]['config']['ch_out']

        print('uuid :',self.uuid,'\nmode :',self.mode,'\nchannel(Input) :',self.ch_in,'\nchanne(output) :',self.ch_out)

    def Setup(self, channel, value):
        print('setup',channel,value)
        if value == GPIO.IN:
            self.ch_in = channel
            print ('channel in : ',self.ch_in)
        elif value == GPIO.OUT:
            self.ch_out = channel
            print ('channel out :',self.ch_out)

    def Output(self, channel, value):
        for i in self.ch_out:
            if i == channel:
                print('detected')
    def Save(self):
        config = {
            hwid.get_uuid() : {
                "config" : {
                    "ch_in" : self.ch_in,
                    "ch_out" : self.ch_out,
                    "mode" : 11
                },
                "setup" : {
                    "17" : 1,
                    "18" : 0,
                    "19" : 0,
                    "20" : 1,
                    "21" : 1
                }
            }
        }
        with open('config.json', 'w') as f:
            json.dump(config, f)

if __name__ == '__main__':
    c = Config()
    # mch_in = [27,22,23,24,25]
    # mch_out = [17,18,]
    # c.Setup(mch_in,GPIO.IN)
    # c.Setup(mch_out,GPIO.OUT)
    # c.Save()
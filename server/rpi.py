import json
import lib.hwid as hwid
import RPi.GPIO as GPIO
from lib.dict import Dictionary

try:
    with open('config.json', 'r') as f:
        data = json.load(f)
        d = Dictionary(data)
        global uuid
        global mode
        global ch_in
        global ch_out

        uuid = hwid.get_uuid()
        mode = d[uuid]['config']['mode']
        ch_in = d[uuid]['config']['ch_in']
        ch_out = d[uuid]['config']['ch_out']

        GPIO.setmode(mode)
        GPIO.getmode()
        GPIO.setup(ch_in,GPIO.IN)
        GPIO.setup(ch_out,GPIO.OUT)
       
except Exception as ex:
    print(ex)
    print('###### build config #######')
    ch_in = []
    ch_in.append(17)
    ch_in.append(18)
    ch_out = []
    ch_out.append(20)
    ch_out.append(21)
    config = {
        hwid.get_uuid() : {
            "config" : {
                "ch_in" : ch_in,
                "ch_out" : ch_out,
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
import json
import hwid as hwid

try:
    with open('config.json', 'r') as f:
        data = json.load(f)
except Exception as ex:
    print(ex)
    print('###### build config #######')
    config = {
        hwid.get_uuid() : {
            "config" : {
                "ch_in" : "{17,18,19}",
                "ch_out" : "{20,21}",
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
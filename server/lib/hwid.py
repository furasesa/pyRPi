import uuid

def get_uuid():
    myuuid = uuid.uuid1()
    a,b,c,d,id = str(myuuid).split('-')
    return id
    # print(e)
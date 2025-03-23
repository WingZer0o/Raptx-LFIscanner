import os

class Checker:
    def get_payload_file(parse):
        path = None
        if parse.operatingsystem == 'linux':
            path = os.path.join(os.getcwd(), 'payloads/linux.txt') 
        elif parse.operatingsystem == 'windows':
            path = os.path.join(os.getcwd(), 'payloads/windows.txt') 
        else:
            path = os.path.join(os.getcwd(), 'payloads/linux.txt') 

        payload = open(path, "r")
        return payload
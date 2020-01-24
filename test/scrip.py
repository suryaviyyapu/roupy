import os
import sys
import requests
import time


url = '192.168.0.1'
usernames = ['admin', '', 'root', 'user', 'cisco', '12345', '1234']
passwords = ['', 'admin', 'password', '1234', '12345', 'cisco']
encoded = ['YWRtaW46MTIzNAo=', 'YWRtaW46cGFzc3dvcmQ=', 'YWRtaW46', 'YWRtaW46YWRtaW4=', 'Y2lzY286Y2lzY28=']
#Loading Encoded Default PASSWORDS
with open('../encodedcreds.txt','r') as readerCreds:
    for line in readerCreds.readlines():
        cred = line.strip('\n')
        print("[+] Trying with "+cred)
        requestToRouter = requests.get(url, headers={"Authorization":"Basic {cred}"})
        #print(requestToRouter.text)
        time.speel(2)
        if 'Base64Encoding' not in requestToRouter.text:
            print(f"Success-"+str({cred}))
            exit(0)
        else:
            print("Invalid")
            exit(0)

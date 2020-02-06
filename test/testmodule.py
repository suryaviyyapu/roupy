import os
import sys
import requests
import time

url = 'https://httpbin.org/headers'
usernames = ['admin', '', 'root', 'user', 'cisco', '12345', '1234']
passwords = ['', 'admin', 'password', '1234', '12345', 'cisco']
encoded = ['YWRtaW46YWRtaW4=', 'YWRtaW46MTIzNAo=', 'YWRtaW46cGFzc3dvcmQ=', 'YWRtaW46', 'Y2lzY286Y2lzY28=']
#Loading Encoded Default PASSWORDS
'''
for line in encoded:
    cred = line.strip('\n')
    print("[+] Trying with "+cred)
    '''
    req = requests.Session()
    requestToRouter = req.get(url, headers={"Authorization":"Basic YWRtaW46YWRtaW4="})
        #print(requestToRouter.text)
    time.sleep(2)
    if 'Base64Encoding' not in requestToRouter.text:
        print(f"Success-")
        exit(0)
    else:
        print("Invalid")

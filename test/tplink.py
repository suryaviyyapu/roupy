import os, sys, requests

#Tested for TP-Link
url = 'http://192.168.0.1'
user = 'admin'
password = '1234'
encoded = 'YWRtaW46YWRtaW4=' 
cook = {'Authorization': 'Basic YWRtaW46MTIzNAo='}
requestToRouter = requests.get(url, cookies=cook)
#print(requestToRouter.text)
if 'Base64Encoding' in requestToRouter.text:
    print("Invalid")
else:
    print("Success "+ encoded)

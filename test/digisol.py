import os, sys, requests
url = 'http://103.125.161.188/login.cgi'
user = 'admin'
password = '1234'
requestToRouter = requests.post(url, data=f"username={user}&password={password}&submit.htm?login.htm=Send", headers={"Content-Type": "application/x-www-form-urlencoded"})
print(requestToRouter.text)
if 'Username or password error' in requestToRouter.text:
    print("Invalid")
else:
    print("Success")

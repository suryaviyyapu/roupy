import os
import sys
import requests
import threading
from routers_info import tplink, digisol, netgear, tenda, dlink
from modules import router_enum_essentials

#Test Creds for Testing
#CONSTANTS
#user = 'admin'
#password = '1234'
MAX_ATTEMPTS = 5
MAX_RETRIES = 3
STATUS = 200
URL_RANGE = "http://"





def chk_connection(URL_RANGE):
   try:
      res = requests.get(URL_RANGE)
   except requests.exceptions.ConnectionError:
      print("No Internet. Exiting")
      exit(0)
   if res.status_code is STATUS:
      print(res.status_code)
      return True
   else:
      print(res.status_code)
      return False

def detect_local_ip():
   os.system('curl ifconfig.me')



def aslr(URL_RANGE):
   pass

def msr(URL_RANGE):
   #pass
   res = requests.get(URL_RANGE)
   responsecode = res.text
   manufacturer, model = router_enum_essentials.router_manufacturer(responsecode)
   print(manufacturer, model)
   if manufacturer is 0:
      print("We don't have this router in our tool.")
   else:
      print("The manufactrer is "+ manufacturer + " Model " + model)
      if manufacturer == 'tplink':
         print("Using TPlink module... ")
         if model == 'Archer C50':
            result = tplink.Archerc50(URL_RANGE)
            if result == True:
               print("Thanks for using Roupy..")
            else:
               print("Sorry we missed this router")

def isr(URL_RANGE):
   pass

if __name__ == '__main__':
   print("Initializing...")
   if len(sys.argv) == 5:
      methodToUse = int(sys.argv[4])
      URL_RANGE = URL_RANGE + sys.argv[2]
      if chk_connection(URL_RANGE):
         if methodToUse is 1:
            #aslr(URL_RANGE)
            pass
         elif methodToUse is 2:
            msr(URL_RANGE)
            #pass
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

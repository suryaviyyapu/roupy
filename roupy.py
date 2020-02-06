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


def aslr(URL_RANGE):
   pass

def msr(URL_RANGE):
   pass

def isr(URL_RANGE):
   pass

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
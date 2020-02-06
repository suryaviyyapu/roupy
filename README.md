#
Roupy is a Python script that is intended for bruteforcing the routers that have default passwords.

##INSTALLATION##
#WINDOWS
pip3 install -r requirements.txt

#Linux
python -m pip3 install -r requirements.txt


#EXEC
python3 roupy.py -u <URL> -t <1|2|3>

-u <URL> URL = The URL to test
-t type of attack you want 
	1. Automatc
	2. Manual
	3. Internet 

##FOR DEVELOPERS##
routers_info folder is a python module with different routers names and those files consists of functions that are used to check for default passwords of that particular router

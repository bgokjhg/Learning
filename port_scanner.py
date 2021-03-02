#!/usr/bin/env python3

import socket
import argparse


def scan(target,port):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(0.1)
		con = s.connect_ex((target,port))
		s.close()
		if con == 0:
			return True
		else:
			return False

def main():
	parser = argparse.ArgumentParser(description="Scanning ports of domains")
	parser.add_argument('-i','--ip',help='Enter ip to scan')
	args = parser.parse_args()
	targ = args.ip
	if args.ip != None:
		for i in range(65535):
			if scan(targ,i):
				print(i,"is open")
	else:
		print("Use ./port_scanner.py -h")

main()



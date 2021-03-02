#!/usr/bin/env python3

import socket
import re
import argparse
import sys
import pyfiglet

def knock(target,ports):
	for p in ports:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		if target == 'loaclhost':
			print("Knocking on",p + "...")
			con = s.connect_ex(('127.0.0.1',int(p)))
			s.close()
		else:
			print("Knocking on",p + "...")
			con = s.connect_ex((target,int(p)))
			s.close()

def check_ip(target):
	if target == 'localhost':
		return True
	else:
		r = re.search('[0-9]{1,3}(\\.[0-9]{1,3}){1,3}',target)
		if r:
			return True
		else:
			print("Please use a valid ip address")
			return False

def check_ports(ports):
	li = []
	for p in ports:
		if re.search('[0-9]{1,5}',p):
			li.append(p)
	return li


def main():
	pyfiglet.print_figlet("	PORT SCANNER",font='standard',colors='LIGHT_GREEN')
	parser = argparse.ArgumentParser(description="Knocking on people's ports")
	parser.add_argument('-i','--ip',help='Enter ip address to knock')
	parser.add_argument('-p','--port',help='Enter port/s seperated by commas')
	args = parser.parse_args()
	if args.ip != None or args.port != None:
		target = args.ip
		c = check_ip(target)
		if c:
			ports = args.port.split(',')
			ports = check_ports(ports)
			knock(target,ports)
	else:
		print("Usage: ./knocker.py -h")

main()

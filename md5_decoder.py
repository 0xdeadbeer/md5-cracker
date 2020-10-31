#!/usr/bin/python3

import os
import sys
import time
import random
import socket
import hashlib


def encode(string, encoding="utf-8"):
	hashmanager = hashlib.md5()
	hashmanager.update(string.encode(encoding).strip())
	return hashmanager.hexdigest()
def crackit(hash, location):
	file = open(location, "r")
	x = 0
	for line in file:
		hashed_line = encode(line)
		if (hashed_line == hash):
			print ("[+] Found match: " + line)
			x = x + 1
			break
	if (x == 0):
		print ("[-] No matches found!!")
def clearTerminal():
	if (os.name == "nt"):
		os.system("cls")
	else:
		os.system("clear")

def showBanner():
	print ("MD5 Decoder")
	print ("Coded by: MrYes2020")
	print ("Usage: ./md5_decoder.py [hash] [wordlist file]")
	print ("Example: ./md5_decoder.py e10adc3949ba59abbe56e057f20f883e /usr/share/wordlists/rockyou.txt")


def main():
	if (len(sys.argv) == 3):
		print ("[!!] Started cracking..")
		hash = sys.argv[1]
		file = sys.argv[2]
		crackit(hash, file)
	else:
		showBanner()
main()


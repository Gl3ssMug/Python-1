#!/usr/bin/python

import os

def decryption(C,d,n):
	P = []
	new = []
	for i in C:
	    new.append((int(int(i)**d))%n)
	for i in new:
		P.append(chr(i))
	return P

def main():
	#FileName = input("Enter The messege file name :")
	FileName = 'Messege.txt'
	fd = open(FileName)
	SampleData = fd.read()
	fd.close()
	os.system("rm -rf "+FileName)

	#FileName = input("Enter Repository name : ")
	FileName = 'Repository.txt'
	fd = open(FileName)
	n = int(fd.readline())
	fd.close()

	s = eval(SampleData)
	print (" old : ",SampleData)
	print ("new : ",s)
	C = []
	for i in s:
	 	C.append(int(ord(i)))
	
	d = int(input("Enter Private Key : "))
	P = decryption(C,d,n)

	print("Messege is : ",str(P).replace(',','')[1:-1])

if __name__ == '__main__':
	main()

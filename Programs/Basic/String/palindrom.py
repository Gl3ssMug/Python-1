#!/usr/bin/python

# problem statement : To check wheather given string is palindrom or not. 

s = input("Enter String")			# accepting string from user

def chk(s):
	if s == s[::-1]:			# comparision between string(s) and reverse of string (s[::-1]) {string slicing}
		return s+" is palindrome"
	else:
		return s+" is not palindrome"
print(chk(s))

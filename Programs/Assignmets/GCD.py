#!/usr/bin/python

def BigSmall(num1,num2):
	if num1 > num2:
		# big = num1
		# small = num2
		return num1,num2
	else:
		# big = num2
		# small = num1
		return num2,num1

def gcd(big,small):
	for i in range(small,1,-1):
		if big % i == 0 and small % i == 0:
		#print ("GCD : ",i)
			return i
	else:
		return 1

def main():
	num1 = int(input("no1 : "))
	num2 = int(input("no2 : "))
	big , small = BigSmall(num1,num2)
	GCD = gcd(big,small)
	print ("GCD is : ",GCD)


if __name__ == '__main__':
	main()

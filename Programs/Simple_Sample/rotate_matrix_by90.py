#!/usr/bin/python
# accept a matrix (image of size n by n pixel )  n rotate it clock wise in 90 degree

def matrix(no,a):							
	for i in range(0,no):		
		a.append([])
		for j in range(0,no):
			val = eval(input("val : "))
			a[i].append(val)
	print (a)

def rorate(no,a,b):
	k = 0
	for j in range(0,no):
		b.append([])
		for i in range(no-1,-1,-1):
			b[j].append(a[i][k])
		k+=1
	print (b)

if __name__ == '__main__':
	no = eval(input("number : "))			# code start accepting the no. of rows and column 
	a = []									# accepting arrays
	b = []
	matrix(no,a)							# calling functions (accepting matrix)
	rorate(no,a,b)							#					(rotating matrix )
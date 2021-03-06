#!/usr/bin/python

# Given ode is for checking plagarism
# accept two file names and compaire each other

def convert(fd1,fd2):
	f = fd1.read()
	f = f.replace('\n',' ')
	f1 = f.split(' ')

	f = fd2.read()
	f = f.replace('\n',' ')
	f2 = f.split(' ')

	return f1,f2

def remove(f1,f2):
	f1 = list(set(f1))
	f2 = list(set(f2))

	return f1,f2

def plagarism(f1,f2):
	c1 = 0
	c2 = 0
	for i in f1:
		if i in f2:
			c1 += 1
	for j in f2:
		if j in f1:
			c2 +=1

	return c1,c2 
			

def main():
	file1 = input(" enter the file name 1 : ")
	file2 = input(" enter the file name 2 : ")

	fd1 = open(file1)
	fd2 = open(file2)

	f1,f2 = convert(fd1,fd2)
	f1,f2 = remove(f1,f2)

	count_f1 = len(f1)
	count_f2 = len(f2)

	f1,f2 = plagarism(f1,f2)
	
	f1 = count_f1 - f1
	f2 = count_f2 - f2

	print (" count 1 {0} f1 {1}  \n count 2 {2} f2 {3}".format(count_f1,f1,count_f2,f2))

	print (" plagarism for file 1 is : {}%".format(f1*100/count_f1))
	print (" plagarism for file 2 is : {}%".format(f2*100/count_f2))

if __name__ == '__main__':
	main()

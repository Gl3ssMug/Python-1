#!/usr/bin/python

import time
import os
import PIL.Image as Image

def ProxyImage():
	img = Image.open("proxy.jpg")
	img.show()
	time.sleep(2)
	img.close()

def RealImage(inputImage):
	img = Image.open(inputImage)
	img.show()

def main():
	inputImage = input("Enter Image Name to Open ")
	statistics = os.stat(inputImage)
	if statistics.st_size > 200:
		print ("loading ...")
		ProxyImage()
	RealImage(inputImage)

if __name__ == '__main__':
	main() 

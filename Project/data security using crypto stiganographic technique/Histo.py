import PIL
from PIL import Image
from matplotlib import pyplot as plt

def hexencode(rgb):
	r=rgb[0]
	g=rgb[1]
	b=rgb[2]
	return '#%02x%02x%02x' % (r,g,b)

def draw(name):
	im = Image.open(name)  
	w, h = im.size  
	colors = im.getcolors(w*h)

	# im1 = Image.open('s1.jpg')  
	# w1, h1 = im1.size  
	# colors1 = im1.getcolors(w1*h1)
	for idx, c in enumerate(colors):
		plt.bar(idx, c[0], color=hexencode(c[1]))

	plt.show()

def main():
	name = str(input("enter the name of image : "))
	
if __name__ == '__main__':
	main()

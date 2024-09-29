from PIL import Image

img = Image.open("a.png")
img.size
img.show()
box =(100,100,400,400)
img2 = img.crop(box) 
img2.show()
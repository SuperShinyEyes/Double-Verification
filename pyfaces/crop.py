from PIL import Image

X = 200
Y = 60
WIDTH = 240
HEIGHT = 320
img = Image.open("image.jpg")
img2 = img.crop((X, Y, X+WIDTH, Y+HEIGHT))
img2.save("img2.jpg")

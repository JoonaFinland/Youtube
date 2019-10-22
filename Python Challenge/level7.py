# The Python Challenge Level 7

from PIL import Image

im = Image.open('oxygen.png')

width, height = im.size

data = [im.getpixel((x, height/2)) for x in range(width)]

data = data[::7]

data = [r for r,g,b,a in data if r == g == b]
data = [105, 110, 116, 101, 103, 114, 105, 116, 121]

for char in data:
    print(chr(char), end='')

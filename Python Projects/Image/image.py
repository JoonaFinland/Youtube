import os
import sys
from PIL import Image, ImageFilter
import argparse

DEFAULT = ''

def save_image(image, path, ext=DEFAULT, overwrite=False, overtag='_new'):
    (name, extension) = os.path.splitext(path)
    things = name.split(os.sep)
    name = things[-1]
    things.pop(-1)
    path = os.sep.join(things)
    if ext!=DEFAULT:
        extension=ext
    else:
        extension = extension[1:]
    if overwrite:
        image.save(path+os.sep+'new'+os.sep+name+'.'+extension.lower())
    else:
        image.save(path+os.sep+'new'+os.sep+name+overtag+'.'+extension.lower())
    print('Saved as:',path+os.sep+'new'+os.sep+name+overtag+'.'+extension.lower())

def resize_image(image, width, height):
    return image.resize((width, height), Image.ANTIALIAS)

def greyscale(image):
    return image.convert('L')

def blur(image):
    return image.filter(ImageFilter.BLUR)

def sharpen(image):
    return image.filter(ImageFilter.SHARPEN)

effects_dict = {
    'blur': blur,
    'sharpen': sharpen,
    'greyscale': greyscale
}

parser = argparse.ArgumentParser(description='Batch Image Manipulator')
parser.add_argument('-d', '--directory', help='The image directory', required=True)
parser.add_argument('-rep', '--replace', help='Output images have same name', required=False, default=False)
parser.add_argument('-ext', '--extension', help='Output image extension', required=False, default='')
parser.add_argument('-fx', '--effects', help='Effects wanted', required=False, default='')
parser.add_argument('-r', '--resize', help='Resize boolean', required=False, default=False)
parser.add_argument('-wi', '--width', help='Width', required=False, default=0)
parser.add_argument('-he', '--height', help='Height', required=False, default=0)
args=parser.parse_args()
rootdir = args.directory
print('Going through images in',rootdir)
effects = args.effects.split(',')
if effects[0] == '':
	effects = []
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        #try:
            #print os.path.join(subdir, file)
            filepath = subdir + os.sep + file
            print(filepath, end=' -> ')
            image = Image.open(filepath)
            for effect in effects:
                if effect in effects_dict:
                    image = effects_dict[effect](image)
                else:
                    print('Effect not implemented')
            if args.resize:
                image = resize_image(image,int(args.width),int(args.height))
            save_image(image, filepath, args.extension, args.replace)
        #except Exception as e:
            #print('Problem opening', filepath, 'e:',e)
    break

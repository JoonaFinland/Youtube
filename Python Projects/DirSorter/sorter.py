import os
import shutil
import sys

dir = sys.argv[1]

files = os.listdir(dir)

for file in files:
    name, ext = os.path.splitext(file)
    ext = ext[1:]
    if ext=='':
        continue
    if os.path.exists(dir+'/'+ext):
        print('moving:',dir+'/'+file,'to:',dir+'/'+ext+'/'+file)
        shutil.move(dir+'/'+file,dir+'/'+ext+'/'+file)
    else:
        os.makedirs(dir+'/'+ext)
        print('moving:',dir+'/'+file,'to:',dir+'/'+ext+'/'+file)
        shutil.move(dir+'/'+file,dir+'/'+ext+'/'+file)

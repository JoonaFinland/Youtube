# The Python Challenge Level 6

import zipfile
import re

name = '90052'
pattern = re.compile('Next nothing is (\d+)')

archive = zipfile.ZipFile('channel.zip', 'r')

comments = []
while True:
    content = archive.read(name+'.txt').decode('utf-8')
    print(content)
    comments.append(archive.getinfo(name+'.txt').comment.decode('utf-8'))
    match = pattern.search(content)
    if match == None:
        break
    name = match.group(1)
    
print(''.join(comments))

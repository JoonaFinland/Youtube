# PythonChallenge Level 4
from webbot import Browser
import re

web = Browser()
#num = '12345'
num = str(16044/2)
link = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='

web.go_to(link + num)

pattern = re.compile('and the next nothing is (\d+)')

while True:
    tmp = web.get_page_source()
    match = pattern.search(tmp)
    new = match.group(1)
    if match == None:
        break
    web.go_to(link + new)
    

# The Python Challenge Level 5

import pickle
from urllib.request import urlopen

raw = urlopen('http://www.pythonchallenge.com/pc/def/banner.p')

data = pickle.load(raw)

for x in data:
    print(''.join([key * val for key, val in x]))

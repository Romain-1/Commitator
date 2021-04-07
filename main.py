#!/usr/bin/env python3

import requests
import shutil
import sys


r=requests.get("https://meme-api.herokuapp.com/gimme")
url = r.json()['url']
while url.split('.')[-1] == "gif":
    r=requests.get("https://meme-api.herokuapp.com/gimme")
    url = r.json()['url']
filename = url.split('/')[-1]
r=requests.get(url)
with open(filename,'wb') as f:
    f.write(r.content)

import sys; from PIL import Image; import numpy as np

chars = np.asarray(list(' .,:;irsXA253hMHGS#9B&@'))
f, SC, GCF, WCF = filename, 0.3, 1, 7/4

img = Image.open(f)
S = ( round(img.size[0]*SC*WCF), round(img.size[1]*SC) )
img = np.sum( np.asarray( img.resize(S) ), axis=2)
img -= img.min()
img = (1.0 - img/img.max())**GCF*(chars.size-1)

print(f"{sys.argv[1]}\n\n" + '\n'.join((''.join(r) for r in chars[img.astype(int)])) + f"\n{url}")

import os

os.remove(filename)

import io
import numpy as np    
from PIL import Image
from os import remove
from json import load, dump

from google_images_search import GoogleImagesSearch

gis = GoogleImagesSearch('[key]', '[password]')

import json















try:
    file = open("dataset.json",mode='r')
except:
    file = open("dataset.json",mode='x')


if file.read()=="":
    _output=[]
    for x in range(0,500):
        _output_1 = []
        for y in range(0,500):
            _output_1.append([])
        _output.append(_output_1)
    dataset=_output
else:
    _dataset=json.load(file)
    dataset=json.loads(_dataset)
file.close()

_search_params = {
    'q': "running",
    'num': 5,
    ##'fileType': 'jpg|gif|png',
    ##'rights': 'cc_publicdomain|cc_attribute|cc_sharealike|cc_noncommercial|cc_nonderived',
    'safe': 'active'
}

# this will only search for images:
gis.search(search_params=_search_params)
for image in gis.results():
    image.download("dataset")
    image.resize(500,500)
    numpydata = np.asarray(Image.open(image.path), dtype='int64')
    prev=[0,0,0,0]
    x=0
    y=0
    decode="RGBL"
    for y_vals in numpydata:
        for x_vals in y_vals:
            data = []
            _next=[]
            for i in range (0,4):
                data.append({decode[i]:int(x_vals[i]-prev[i])})
                _next.append(int(x_vals[i]-prev[i]))
            dataset[y][x].append(data)
            prev=_next
            x+=1
        prev=list(numpydata[y][x-1])
        y+=1
        x=0

    file = open("dataset.json",mode='w')
    jsout=json.dumps(dataset)
    json.dump(jsout,file)
    print(file)
    file.close()

    

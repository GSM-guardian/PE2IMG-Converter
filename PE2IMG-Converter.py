import sys
import os
from core.reader import *
from core.draw import *

print('PE2IMG-Converter')

PATH = input('PATH >> ')
dataList = getDataList(PATH)

if not os.path.isdir(PATH):
    print('PATH is not dir')
else:
    for data in dataList:
        dataPath = PATH + '/' + data
        drawImg(dataPath, getRaw(dataPath))
        print(data + ' drawing to PNG image...')
    print('Done!')
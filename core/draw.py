import cv2
import os 
import numpy
import hashlib
from .reader import getFileInfo
from .log import *

def drawImg(PATH, RAW):
    imgVector = RAW
    fileInfo = getFileInfo(PATH)
    sizeOfFile = fileInfo['sizeOfFile'] / 1024 # Save in KB

    fileName = fileInfo['fileName']
    encFileName = hashlib.md5()

    if fileInfo['extensionCheck'] == False:
        print(fileName + ' is not PE Format')

    # Hashing filename for img filename
    encFileName.update(fileName.encode('utf-8'))
    imgFileName = encFileName.hexdigest()     

    # Specify width according to file capacity
    if sizeOfFile < 10:
        width = 32
    elif sizeOfFile >= 10 and sizeOfFile < 30:
        width = 64
    elif sizeOfFile >= 30 and sizeOfFile < 60:
        width = 128
    elif sizeOfFile >= 60 and sizeOfFile < 100:
        width = 256
    elif sizeOfFile >= 100 and sizeOfFile < 200:
        width = 384
    elif sizeOfFile >= 200 and sizeOfFile < 500:
        width = 512
    elif sizeOfFile >= 500 and sizeOfFile < 1000:
        width = 768
    else:
        width = 1024

    # ValueError Handler
    if len(imgVector) % width != 0:
        while True:
            imgVector.append(0)
            if len(imgVector) % width == 0:
                break

    # Output 2D Vector array to image
    imgPixArray = numpy.reshape(imgVector, (-1, width))
    cv2.imwrite(imgFileName + '.png', imgPixArray)
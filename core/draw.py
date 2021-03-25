import cv2 
import numpy as np
import hashlib as hs
import core.reader as rd


def drawImg(PATH, RAW):
    fileInfo = rd.getFileInfo(PATH)
    sizeOfFile = fileInfo['sizeOfFile'] / 1024 # Save in KB
    fileName = fileInfo['fileName']
    raw = RAW 

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
    if len(raw) % width != 0:
        while len(raw) % width == 0:
            raw.append(0)

    # Output raw array to image
    imgPixArray = np.reshape(raw, (-1, width))
    cv2.imwrite('test.jpg', imgPixArray)

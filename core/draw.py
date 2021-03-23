import cv2 
import numpy as np
import os

def drawingImg(PATH, RAW):
    SizeOfFile = os.path.getsize(PATH) / 1024
    width = 0
    raw = RAW

    if SizeOfFile < 10:
        width = 32
    elif SizeOfFile >= 10 and SizeOfFile < 30:
        width = 64
    elif SizeOfFile >= 30 and SizeOfFile < 60:
        width = 128
    elif SizeOfFile >= 60 and SizeOfFile < 100:
        width = 256
    elif SizeOfFile >= 100 and SizeOfFile < 200:
        width = 384
    elif SizeOfFile >= 200 and SizeOfFile < 500:
        width = 512
    elif SizeOfFile >= 500 and SizeOfFile < 1000:
        width = 768
    else:
        width = 1024

    if  len(raw) % width != 0:
        while True:
            if len(raw) % width == 0:
                break
            raw.append(0)

    ImgBitArray = np.reshape(RAW, (-1, width))
    print(len(RAW))
    cv2.imwrite('test.png', ImgBitArray)

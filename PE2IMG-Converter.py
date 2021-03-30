import sys
import os
from core.reader import getDataList, getRaw
from core.draw import drawImg

def main():
    print('PE2IMG-Converter v1.0')

    PATH = input('PATH >> ')

    if os.path.isdir(PATH) != True:
        print('PATH is not dir')
        sys.exit()

    dataList = getDataList(PATH)

    for data in dataList:
        dataPath = PATH + '/' + data
        drawImg(dataPath, getRaw(dataPath))
        print(data + ' drawing to PNG image...')
    print('Done!')

if __name__ == '__main__':
    main()
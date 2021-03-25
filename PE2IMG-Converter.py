from core.reader import *
from core.draw import *

print('PE2IMG-Converter')
PATH = input('PATH >> ')

getFileInfo(PATH)
drawImg(PATH, getRaw(PATH))
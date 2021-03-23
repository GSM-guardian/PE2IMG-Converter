from core.reader import *
from core.draw import *

print('PE2IMG-Converter')
PATH = input('PATH >> ')

drawingImg(PATH, GetRaw(PATH))
GetInfo(PATH)
ExtensionsCheck(PATH)
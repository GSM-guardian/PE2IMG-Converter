import sys
import core.reader as rd
import core.draw as dr

print('PE2IMG-Converter')
PATH = input('PATH >> ')
rd.getFileInfo(PATH)
dr.drawImg(PATH, rd.getRaw(PATH))

# if len(sys.argv) != 2:
#     print('')
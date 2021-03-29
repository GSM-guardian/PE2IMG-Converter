import time, os

def getDataList(PATH):
    dataList = os.listdir(PATH)
    return dataList

def getRaw(PATH): 
    with open(PATH, 'rb') as f01:
        raw = bytearray(f01.read())
    return raw

def getFileInfo(PATH):
    sizeOfFile = os.path.getsize(PATH)
    extensions = ['exe', 'scr', 'sys', 'vxd', 'dll', 'ocx', 'cpl', 'drv', 'obj']
    extensionCheck = False
    raw = getRaw(PATH)
    fileName = PATH.split('/')
    
    # Extenstion Check
    for extension in extensions:
        if PATH[-3:] == extension:
            extensionCheck = True
            break

    return {
        'PATH': PATH,
        'fileName': fileName[len(fileName) - 1],
        'extensionCheck': extensionCheck,
        'sizeOfFile': sizeOfFile,
        'lengthOfRAW': len(raw),
        }
import time, os

def getRaw(PATH): 
    with open(PATH, 'rb') as f01:
        raw = bytearray(f01.read())
    return raw

def getFileInfo(PATH):
    sizeOfFile = os.path.getsize(PATH)
    extensions = ['exe', 'scr', 'sys', 'vxd', 'dll', 'ocx', 'cpl', 'drv', 'obj']
    extensionCheck = False
    raw = getRaw(PATH)
    
    # Extenstion Check
    for i in range(0, len(extensions)):
        if PATH[-3:] == extensions[i]:
            extensionCheck = True
            break

    return {
        'PATH': PATH,
        'extensionCheck': extensionCheck,
        'sizeOfFile': sizeOfFile,
        'lengthOfRAW': len(raw),
        }
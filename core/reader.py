import time, os

def ExtensionsCheck(PATH):
    extensions = ['exe', 'scr', 'sys', 'vxd', 'dll', 'ocx', 'cpl', 'drv', 'obj']
    for i in range(0, len(extensions)):
        if PATH[-3:] == extensions[i]:
            print(f'extension check : {PATH} - P')
            break
        elif PATH[-3:] != extensions[len(extensions) - 1]:
            print(f'extension check : {PATH} - N')

def GetRaw(PATH): 
    # offsetNum = 0
    # timeToStart = time.time()
    with open(PATH, 'rb') as f01:
        raw = bytearray(f01.read())
    # for i in range(0, int(len(raw) / 16)): 
    #     if offsetNum == 256: 
    #         break
    #     print('\n%07X0  | ' % offsetNum, end='') 
    #     offsetNum += 1 
    #     for j in range(0, 16): 
    #         print('%02X' % raw[i * 16 + j], end=' ') 
    # print('\nDone!\nTotal Running time : %.2f ms' % (1000 * (time.time() - timeToStart)))
    return raw

def GetSizeOfFile(PATH):
    return os.path.getsize(PATH) / 1024

def GetInfo(PATH):
    SizeOfFile = os.path.getsize(PATH)
    with open(PATH, 'rb') as f01:
        raw = bytearray(f01.read())
    print(f'Length of raw (8bit) : {len(raw)}')
    print(f'Size of File (KB) : {SizeOfFile / 1024} KB')
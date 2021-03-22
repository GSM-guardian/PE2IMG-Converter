def ExtensionsCheck(PATH):
    extensions = ['exe', 'scr', 'sys', 'vxd', 'dll', 'ocx', 'cpl', 'drv', 'obj']
    for i in range(0, len(extensions)):
        if PATH[-3:] == extensions[i]:
            print(f'extension check : {PATH} - P')
            break
        elif PATH[-3:] != extensions[len(extensions) - 1]:
            print(f'extension check : {PATH} - N')
def GetRaw(PATH): 
    offsetNum = 0 
    with open(PATH, 'rb') as f01:
        raw = bytearray(f01.read())
    for i in range(0, int(len(raw) / 16)): 
        if offsetNum == 16: 
            break
        print('\n%07X0  | ' % offsetNum, end='') 
        offsetNum += 1 
        for j in range(0, 16): 
            print('%02X' % raw[i * 16 + j], end=' ') 
    print('\n--Done--')
def GetInfo(PATH):
    with open(PATH, 'rb') as f01:
        raw = bytearray(f01.read())
    print(f'length of raw(8bit) : {len(raw)}')
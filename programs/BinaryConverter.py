ifile = open('Rect.hack', 'r')
ofile = open('Rect.hex', 'w')

lines = ifile.readlines()

ofile.write('v3.0 hex bytes plain big-endian\n')

for line in lines:
    #print(hex(int(line[0:8], 2)).lstrip("0x").zfill(2))
    #print(hex(int(line[8:16], 2)).lstrip("0x").zfill(2))
    ofile.write(hex(int(line[0:8], 2)).lstrip("0x").zfill(2))
    ofile.write(hex(int(line[8:16], 2)).lstrip("0x").zfill(2))
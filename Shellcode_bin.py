import os
#this will convert shellcode to bin file for shellcode analysis
print "*****Shellcode To Hex ANd Bin****"
from binascii import unhexlify as unhx

encoded = open('shell.txt').read() # The shellcode dump
out = open('shellcode.bin', 'wb')

for s in encoded.split('%'):
    if len(s) == 5:
        HI_BYTE = s[3:]
        LO_BYTE = s[1:3]
        out.write(unhx(HI_BYTE))
        out.write(unhx(LO_BYTE))
out.close()

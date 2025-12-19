from Q1patternencrypted import *
from Q1patterndecrypted import *

shift1 = int(input ('shift1: '))
shift2 = int(input('shift2: '))

def compare():
    with    open('raw_text.txt','r',encoding='utf-8') as rawtext, \
            open('decrypted_text.txt','r',encoding='utf-8') as decrypted:

        rawdata = rawtext.read()
        decrypteddata= decrypted.read()

        if rawdata == decrypteddata:
            print(True)
        else:
            print(False)

encryptedfunction(shift1,shift2)
decryptedfunction(shift1,shift2)
compare()
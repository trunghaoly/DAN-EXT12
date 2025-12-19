# Import custom modules
from Q1keyencrypted import *
from Q1keydecrypted import *

# Get user input
shift1 = int(input ('shift1: '))
shift2 = int(input('shift2: '))
def compare():
    """
    Verifies if the decrypted text matches the original raw text.
    """

    # Open files for verification
    with    open('raw_text.txt','r',encoding='utf-8') as rawtext, \
            open('decrypted_text.txt','r',encoding='utf-8') as decrypted:
    
    # Read content
        rawdata = rawtext.read()
        decrypteddata = decrypted.read()
    
    # Compare and print result
        if rawdata == decrypteddata:
            print(True)
        else:
            print(False)

# Execute workflow
key = encrypted_function(shift1,shift2)
decrypted_function(key,shift1,shift2)
compare()
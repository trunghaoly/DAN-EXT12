def encrypted_function(shift1,shift2):
    """
    Encrypts 'raw_text.txt' using shift values and saves to 'encrypted_text.txt'.
    Returns the key string required for decryption.
    """

    # Initialize key
    key =''
    
    # Open files to read and write
    with    open('raw_text.txt','r',encoding='utf-8') as rawtext, \
            open('encrypted_text.txt','w',encoding='utf-8') as encrypted :
        
        # Encrypt line by line
        for line in rawtext:
            store1 =''
            
            # Process each character
            for i in line:
                if 'a' <= i <= 'm':
                    store1 += chr((ord(i) - ord('a') + (shift1*shift2)) % 26 + ord('a'))
                    key += '1'
                elif 'n' <= i <= 'z':
                    store1 += chr((ord(i) - ord('a') - (shift1+shift2)) % 26 + ord('a'))
                    key += '2'
                elif 'A' <= i <= 'M':
                    store1 += chr((ord(i) - ord('A') - shift1) % 26 + ord('A'))
                    key += '3'
                elif 'N' <= i <= 'Z':
                    store1 += chr((ord(i) - ord('A') + shift2**2) % 26 + ord('A'))
                    key += '4'
                elif i =='\n':
                    store1 += '\n'
                    key += '5'
                else:
                    store1 += i
                    key += '6'
            
            # Save result
            encrypted.write(store1)
    return key
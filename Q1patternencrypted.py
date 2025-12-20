def encryptedfunction(shift1,shift2):
    """
    Encrypts 'raw_text.txt' using shift values and saves to 'encrypted_text.txt'.
    Returns the key string required for decryption and saves to 'pattern'.
    """

    # Open files to read and write
    with    open('raw_text.txt','r',encoding='utf-8') as rawtext, \
            open('encrypted_text.txt','w',encoding='utf-8') as encrypted, \
            open('pattern','w') as pattern:
        
        # Encrypt line by line
        for line in rawtext:
            
            # Initialize key
            store1 =''
            
            # Process each character
            for i in line:
                if 'a' <= i <= 'm':
                    store1 += chr((ord(i) - ord('a') + (shift1*shift2)) % 26 + ord('a'))
                    pattern.write('1')
                elif 'n' <= i <= 'z':
                    store1 += chr((ord(i) - ord('a') - (shift1+shift2)) % 26 + ord('a'))
                    pattern.write('2')
                elif 'A' <= i <= 'M':
                    store1 += chr((ord(i) - ord('A') - shift1) % 26 + ord('A'))
                    pattern.write('3')
                elif 'N' <= i <= 'Z':
                    store1 += chr((ord(i) - ord('A') + shift2**2) % 26 + ord('A'))
                    pattern.write('4')
                elif i =='\n':
                    store1 += i
                    pattern.write('\n')
                else:
                    store1 += i
                    pattern.write('5') 
            
            # Save result
            encrypted.write(store1)
def decrypted_function(key,shift1,shift2):
    """
    Decrypts content from file using key and shift values.
    """
    
    # Open files to read and write
    with    open('encrypted_text.txt','r',encoding='utf-8') as encrypted, \
            open('decrypted_text.txt','w',encoding='utf-8') as decrypted:
        
        # Read content
        file_encrypted = encrypted.read()
        store2 =''
        
        # Decrypt character by character
        for i,k in zip(file_encrypted,key):
                if k == '1':
                    store2 += chr((ord(i) - ord('a') - (shift1*shift2)) % 26 + ord('a'))
                elif k == '2':
                    store2 += chr((ord(i) - ord('a') + (shift1+shift2)) % 26 + ord('a'))
                elif k =='3':
                    store2 += chr((ord(i) - ord('A') + shift1) % 26 + ord('A'))
                elif k == '4':
                    store2 += chr((ord(i) - ord('A') - shift2**2) % 26 + ord('A'))
                elif k == '5':
                    store2 += '\n'
                else:
                    store2 += i
        
        # Save result
        decrypted.write(store2)

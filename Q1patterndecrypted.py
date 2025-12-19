def decryptedfunction(shift1,shift2):
    with    open('encrypted_text.txt','r',encoding='utf-8') as encrypted, \
            open('decrypted_text.txt','w',encoding='utf-8') as decrypted, \
            open('pattern','r') as pattern:

        for line1, line2 in zip(encrypted,pattern):
            store2 =''
            for i,k in zip(line1,line2):
                if k == '1':
                    store2 += chr((ord(i) - ord('a') - (shift1*shift2)) % 26 + ord('a'))
                elif k == '2':
                    store2 += chr((ord(i) - ord('a') + (shift1+shift2)) % 26 + ord('a'))
                elif k =='3':
                    store2 += chr((ord(i) - ord('A') + shift1) % 26 + ord('A'))
                elif k == '4':
                    store2 += chr((ord(i) - ord('A') - shift2**2) % 26 + ord('A'))
                else:
                    store2 += i
            decrypted.write(store2)
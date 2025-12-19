def encryptedfunction(shift1,shift2):
    with    open('raw_text.txt','r',encoding='utf-8') as rawtext, \
            open('encrypted_text.txt','w',encoding='utf-8') as encrypted, \
            open('pattern','w') as pattern:
        for line in rawtext:
            store1 =''
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
            encrypted.write(store1)
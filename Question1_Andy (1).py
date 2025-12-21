import filecmp

RAW_FILE = "raw_text.txt"
ENCRYPTED_FILE = "encrypted_text.txt"
DECRYPTED_FILE = "decrypted_text.txt"


def shift_char(c, shift):
    """
    Shift a single alphabetic character by `shift` positions, wrapping A-Z or a-z.
    Non-alphabetic characters are returned unchanged.
    """
    if "a" <= c <= "z":
        base = ord("a")
        return chr((ord(c) - base + shift) % 26 + base)
    elif "A" <= c <= "Z":
        base = ord("A")
        return chr((ord(c) - base + shift) % 26 + base)
    else:
        return c


def encrypt_text(text, shift1, shift2):
    """
    Encrypt text with category markers embedded.
    
    Rules:
    - Lowercase a-m: shift forward by shift1
    - Lowercase n-z: shift forward by shift2
    - Uppercase A-M: shift backward by shift1
    - Uppercase N-Z: shift backward by shift2
    - Other characters: unchanged
    
    Markers encode which category each character came from.
    """
    encrypted = []
    
    for c in text:
        if "a" <= c <= "z":
            if "a" <= c <= "m":  # lowercase first half
                shift = shift1
                encrypted.append('1')  # marker
            else:  # lowercase second half (n-z)
                shift = shift2
                encrypted.append('2')  # marker
            encrypted.append(shift_char(c, shift))
            
        elif "A" <= c <= "Z":
            if "A" <= c <= "M":  # uppercase first half
                shift = -shift1
                encrypted.append('3')  # marker
            else:  # uppercase second half (N-Z)
                shift = -shift2
                encrypted.append('4')  # marker
            encrypted.append(shift_char(c, shift))
            
        else:  # Spaces, digits, special characters
            encrypted.append('0')  # marker for non-letter
            encrypted.append(c)
    
    return "".join(encrypted)


def decrypt_text(text, shift1, shift2):
    """
    Decrypt text using the embedded category markers.
    """
    decrypted = []
    i = 0
    
    while i < len(text):
        marker = text[i]
        i += 1
        
        if marker == '1':  # lowercase first half
            c = text[i]
            decrypted.append(shift_char(c, -shift1))
            i += 1
        elif marker == '2':  # lowercase second half
            c = text[i]
            decrypted.append(shift_char(c, -shift2))
            i += 1
        elif marker == '3':  # uppercase first half
            c = text[i]
            decrypted.append(shift_char(c, shift1))
            i += 1
        elif marker == '4':  # uppercase second half
            c = text[i]
            decrypted.append(shift_char(c, shift2))
            i += 1
        elif marker == '0':  # non-letter
            decrypted.append(text[i])
            i += 1
    
    return "".join(decrypted)


def encrypt_file(shift1, shift2):
    """Read raw_text.txt, encrypt it, and write to encrypted_text.txt."""
    try:
        with open(RAW_FILE, "r", encoding="utf-8") as f:
            raw_text = f.read()
    except FileNotFoundError:
        print(f"Error: {RAW_FILE} not found.")
        return False

    encrypted_text = encrypt_text(raw_text, shift1, shift2)

    with open(ENCRYPTED_FILE, "w", encoding="utf-8") as f:
        f.write(encrypted_text)
    
    return True


def decrypt_file(shift1, shift2):
    """Read encrypted_text.txt, decrypt it, and write to decrypted_text.txt."""
    try:
        with open(ENCRYPTED_FILE, "r", encoding="utf-8") as f:
            encrypted_text = f.read()
    except FileNotFoundError:
        print(f"Error: {ENCRYPTED_FILE} not found.")
        return False

    decrypted_text = decrypt_text(encrypted_text, shift1, shift2)

    with open(DECRYPTED_FILE, "w", encoding="utf-8") as f:
        f.write(decrypted_text)
    
    return True


def verify_decryption():
    """
    Compare raw_text.txt with decrypted_text.txt and report whether they match.
    """
    try:
        same = filecmp.cmp(RAW_FILE, DECRYPTED_FILE, shallow=False)
        if same:
            print("✓ Decryption successful: decrypted_text.txt matches raw_text.txt")
            return True
        else:
            print("✗ Decryption FAILED: files do not match")
            return False
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return False


def main():
    print("=== Encryption/Decryption Program ===\n")
    
    # 1. Prompt the user for shift1 and shift2
    while True:
        try:
            shift1 = int(input("Enter shift1 (integer): "))
            shift2 = int(input("Enter shift2 (integer): "))
            break
        except ValueError:
            print("Both shift1 and shift2 must be integers. Please try again.\n")

    # 2. Encrypt the contents of raw_text.txt
    print(f"\nEncrypting {RAW_FILE} with shift1={shift1}, shift2={shift2}...")
    if not encrypt_file(shift1, shift2):
        return
    print(f"✓ Encrypted content written to {ENCRYPTED_FILE}")

    # 3. Decrypt the encrypted file
    print(f"\nDecrypting {ENCRYPTED_FILE}...")
    if not decrypt_file(shift1, shift2):
        return
    print(f"✓ Decrypted content written to {DECRYPTED_FILE}")

    # 4. Verify the decryption
    print(f"\nVerifying decryption...")
    verify_decryption()


if __name__ == "__main__":
    main()

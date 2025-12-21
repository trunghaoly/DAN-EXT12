# Import custom modules
from Q1keyencrypted import *
from Q1keydecrypted import *

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
            print('SUCCESS: The decrypted text matches the original.')
        else:
            print('FAILURE: The content does not match.')

def main():

    # Loop until the user provides valid integer inputs
    while True:
        try:
            shift1 = int(input('shift1: '))
            shift2 = int(input('shift2: '))
            break
        except ValueError:
                print('Error: Please enter valid integers for shifts.')

    # Execute workflow
    try:
        print("--- Encrypting ---")
        key = encrypted_function(shift1, shift2)
        
        print("--- Decrypting ---")
        decrypted_function(key, shift1, shift2)
        
        print("--- Comparing ---")
        compare()

    # Handle potential errors (Missing files, etc.)    
    except FileNotFoundError:
        print('Error: One of the required files was not found')
    except Exception as i:
        print(f'An unexpected error occurred: {i}')

# Check if the script is being run directly (not imported)
if __name__ == "__main__":
    main()
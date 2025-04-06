letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)

def cipher(mode, text, key):
    result = ''
    if mode == '2':
        key = -key
    for letter in text:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                result += letter
            else: 
                new_index = index + key
                if new_index >= num_letters:
                    new_index -= num_letters
                elif new_index <0:
                     new_index += num_letters
                result += letters[new_index]
    return result


print()
print('CAESAR CIPHER PROGRAM')
print()

print('1. Encrypt')
print('2. Decrypt')

mode = input('Put in the number of the program you wish to use: ')
print()

if mode == '1':
    print('ENCRYPTION MODE')
    print()
    key = int(input('Enter the key of encryption (1-26): '))
    text = input('Enter the text to encrypt: ')
    ciphertext = cipher(mode,text,key)
    print(f'Encrypted text : {ciphertext}')

elif mode == '2':
    print('DECRYPTION MODE')
    print()
    key = int(input('Enter the key of encryption (1-26): '))
    text = input('Enter the text to decrypt: ')
    plaintext = cipher(mode,text,key)
    print(f'Decrypted text : {plaintext}')

else :
    print('Error! Please put in either 1 for encryption or 2 for decryption')

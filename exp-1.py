# Ceaser Cipher Encryption and Decryption

text = input("Enter the text: ")
shift = int(input("Enter the number of shift: "))

def ceaser_encrypt(text, shift):
    result = ""
    shift = shift % 26

    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            new_pos = (ord(char) - base + shift) % 26
            result += chr(base + new_pos)
        else:
            result += char

    return result

def ceaser_decrypt(text, shift):
    result = ""
    shift = shift % 26

    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            new_pos = (ord(char) - base - shift) % 26
            result += chr(base + new_pos)
        else:
            result += char

    return result

ciphertext = ceaser_encrypt(text, shift)
plaintext = ceaser_decrypt(ciphertext, shift)

print("Ciphertext =", ciphertext)
print("Plaintext =", plaintext)

# Vigenere Cipher Encryption and Decryption

plaintext = input("Enter the text: ")
key = input("Enter your key to encrypt: ")

# Encryption : 

def vigenere_encrypt(plaintext, key):
    result = ""
    j = 0

    for ch in plaintext:
        if ch.isalpha():

            p = ord(ch.upper()) - ord("A")
            k = ord(key[j].upper()) - ord("A")

            c = (p + k) % 26

            if ch.isupper():
                result += chr(c + ord("A"))
            else:
                result += chr(c + ord("a"))

            j += 1

            if j == len(key):
                j = 0

        else:
            result += ch

    return result

# Decryption :

def vigenere_decrypt(ciphertext, key):
    result = ''
    j = 0
    key = key.upper()

    for ch in ciphertext:
        if ch.isalpha():
            p = ord(ch.upper()) - ord("A")
            k = ord(key[j].upper()) - ord("A")
            c = (p - k) % 26

            if ch.isupper():
                result += chr(c + ord("A"))
            else:
                result += chr(c + ord("a"))

            j += 1

            if j == len(key):
                j = 0

        else:
            result += ch

    return result

ciphertext = vigenere_encrypt(plaintext, key)
plaintext = vigenere_decrypt(ciphertext, key)

print(f"cihpertext = ", ciphertext)
print(f"plaintext = ", plaintext)

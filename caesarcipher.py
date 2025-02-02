alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

def encrypt(orignalText, timesToBeShifted):
    cipherText = ""
    for letter in orignalText:
        if letter in alphabet:
            position = alphabet.index(letter) + timesToBeShifted
            cipherText += alphabet[position]
    return cipherText

def decrypt(cipherText, timesShifted):
    originalText = ""
    for letter in cipherText:
        if letter in alphabet:
            position = alphabet.index(letter) - timesShifted
            originalText += alphabet[position]
    return originalText

if direction == 'encode':
    result = encrypt(text, shift)
    print(f"Encoded message: {result}")
elif direction == 'decode':
    result = decrypt(text, shift)
    print(f"Decoded message: {result}")
else:
    print("Invalid type")

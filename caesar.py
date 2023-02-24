import sys

def encipher(key):     
    plain_text = input("Enter the plain-text: ")      #NOT RUNNING THE WAY I WANT IT TO WORK
    cipher_text = ""

    for i in range(len(plain_text)):
        if plain_text[i].isalpha():
            index = ord(plain_text[i]) + (ord('A') if plain_text[i].isupper() else ord('a'))
            cipher_temp = (index + key) % 26
            cipher_char = chr(cipher_temp + (ord('A') if plain_text[i].isupper() else ord('a')) - (ord('A') if plain_text[i].isupper() else ord('a')))
            cipher_text += cipher_char
        else:
            cipher_text += plain_text[i]

    print(cipher_text)

if __name__ == "__main__":
    if len(sys.argv) < 2 or not sys.argv[1].isdigit():
        print("Usage: ceasar key")
        sys.exit(1)

    key = int(sys.argv[1])
    encipher(key)

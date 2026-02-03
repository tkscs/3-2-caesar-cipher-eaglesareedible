import string

# This will give you a string with all the lowercase letters in the alphabet
alphabet = string.ascii_lowercase
print(f"{alphabet = }")

ascii_number = ord("d")
print(f"ascii number representation of 'd': {ascii_number}")

ascii_letter = chr(97)
print(f"ascii letter at position #97: {ascii_letter}")

plaintext = "This is a secret message."

# Initialize your ciphertext an empty string
ciphertext = ""
for character in plaintext.lower():
    try:
        encrypted_character = alphabet[(alphabet.index(character) + 1)%26]
    except:
        encrypted_character = character
    ciphertext += encrypted_character

print(f"{ciphertext = }")

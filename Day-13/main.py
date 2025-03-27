def encrypt_message(message, shift):
    encrypted = ""
    for char in message:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower() and shifted > ord('z') or char.isupper() and shifted > ord('Z'):
                shifted -=26
            encrypted += chr(shifted)
        else:
            encrypted += char
    return encrypted
def decrypt_message(encrypted, shift):
    return encrypt_message(encrypted, -shift)
message = input("Enter Your Message: ")
shift = 3
encrypted_message = encrypt_message(message, shift)
print(f"Encrypted: {encrypted_message}")

decrypted_message = decrypt_message(encrypted_message, shift)
print(f"Decrypted: {decrypted_message}")

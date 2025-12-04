import string

def caesar_encrypt(message, key):
    shift = key % 26
    cipher = str.maketrans(string.ascii_lowercase , string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])
    encrypted_message = message.lower().translate(cipher)
    return encrypted_message
def caesar_decrypt(encrypted_message, key):
    shift = 26 - (key % 26)
    cipher = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift])
    messsage = encrypted_message.translate(cipher)
    return messsage
message = input("Enter the message to encrypt: ")
key = 3
encrypted_message = caesar_encrypt(message, key)
print(f"encrypted_message: {encrypted_message}")
decrypted_message = caesar_decrypt(encrypted_message, key)
print(f"decrypted_message: {decrypted_message}")

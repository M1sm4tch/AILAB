from Crypto.Cipher import AES, DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def aes_encrypt(key, plaintext):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    return ciphertext, cipher.iv

def aes_decrypt(key, ciphertext, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext

def des_encrypt(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext, DES.block_size))
    return ciphertext

def des_decrypt(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    plaintext = unpad(cipher.decrypt(ciphertext), DES.block_size)
    return plaintext

# Example usage
aes_key = get_random_bytes(16)  # AES key must be 16, 24, or 32 bytes long
des_key = get_random_bytes(8)   # DES key must be 8 bytes long

plaintext = b"Hello, World!"

# AES Encryption
aes_ciphertext, aes_iv = aes_encrypt(aes_key, plaintext)
print("AES Encrypted:", aes_ciphertext.hex())

# AES Decryption
aes_decrypted = aes_decrypt(aes_key, aes_ciphertext, aes_iv)
print("AES Decrypted:", aes_decrypted.decode())

# DES Encryption
des_ciphertext = des_encrypt(des_key, plaintext)
print("DES Encrypted:", des_ciphertext.hex())

# DES Decryption
des_decrypted = des_decrypt(des_key, des_ciphertext)
print("DES Decrypted:", des_decrypted.decode())

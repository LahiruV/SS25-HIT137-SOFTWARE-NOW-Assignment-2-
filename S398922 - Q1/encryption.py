import os

# -------- FILE PATHS --------
RAW_FILE = r"C:/Users/syeds/Downloads/SN GIT/SS25-HIT137-SOFTWARE-NOW-Assignment-2-/S398922 - Q1/raw_text.txt"
ENCRYPTED_FILE = "encrypted_text.txt"
DECRYPTED_FILE = "decrypted_text.txt"

def encrypt_char(ch, shift1, shift2):
    # Process Lowercase: shift forward by shift1
    if 'a' <= ch <= 'z':
        pos = ord(ch) - ord('a')
        new_pos = (pos + shift1) % 26
        return chr(new_pos + ord('a'))
    
    # Process Uppercase: shift forward by shift2
    elif 'A' <= ch <= 'Z':
        pos = ord(ch) - ord('A')
        new_pos = (pos + shift2) % 26
        return chr(new_pos + ord('A'))
    
    # Return special characters (spaces, punctuation) unchanged
    return ch

def decrypt_char(ch, shift1, shift2):
    # Process Lowercase: shift backward by shift1
    if 'a' <= ch <= 'z':
        pos = ord(ch) - ord('a')
        new_pos = (pos - shift1) % 26
        return chr(new_pos + ord('a'))
    
    # Process Uppercase: shift backward by shift2
    elif 'A' <= ch <= 'Z':
        pos = ord(ch) - ord('A')
        new_pos = (pos - shift2) % 26
        return chr(new_pos + ord('A'))
    
    # Return special characters unchanged
    return ch
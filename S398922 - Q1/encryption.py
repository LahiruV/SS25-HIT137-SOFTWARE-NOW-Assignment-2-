"""
This program performs file encryption and decryption
using a simple character shifting technique.
Lowercase and uppercase letters are shifted differently,
while special characters remain unchanged.
"""

import os

# -------- FILE PATHS --------
RAW_FILE = r"C:/Users/syeds/Downloads/SN GIT/SS25-HIT137-SOFTWARE-NOW-Assignment-2-/S398922 - Q1/raw_text.txt"
ENCRYPTED_FILE = "encrypted_text.txt"
DECRYPTED_FILE = "decrypted_text.txt"


def encrypt_char(ch, shift1, shift2):
    """
    Encrypts a single character.

    Lowercase letters are shifted using shift1.
    Uppercase letters are shifted using shift2.
    Special characters are returned as it is.
    """
    if 'a' <= ch <= 'z':
        pos = ord(ch) - ord('a')
        new_pos = (pos + shift1) % 26
        return chr(new_pos + ord('a'))

    elif 'A' <= ch <= 'Z':
        pos = ord(ch) - ord('A')
        new_pos = (pos + shift2) % 26
        return chr(new_pos + ord('A'))

    return ch


def decrypt_char(ch, shift1, shift2):
    """
    Decrypts a single character.

    This function reverses the encryption
    by shifting characters in the opposite direction.
    """
    if 'a' <= ch <= 'z':
        pos = ord(ch) - ord('a')
        new_pos = (pos - shift1) % 26
        return chr(new_pos + ord('a'))

    elif 'A' <= ch <= 'Z':
        pos = ord(ch) - ord('A')
        new_pos = (pos - shift2) % 26
        return chr(new_pos + ord('A'))

    return ch


def encrypt_file(shift1, shift2):
    """
    Reads the raw text file and writes
    the encrypted content into another file.
    """
    if not os.path.exists(RAW_FILE):
        print(f"File not found: {RAW_FILE}")
        return

    with open(RAW_FILE, "r") as f:
        text = f.read()

    encrypted = "".join(encrypt_char(c, shift1, shift2) for c in text)

    with open(ENCRYPTED_FILE, "w") as f:
        f.write(encrypted)


def decrypt_file(shift1, shift2):
    """
    Reads the encrypted file and converts it
    back to the original text using decryption.
    """
    if not os.path.exists(ENCRYPTED_FILE):
        return

    with open(ENCRYPTED_FILE, "r") as f:
        text = f.read()

    decrypted = "".join(decrypt_char(c, shift1, shift2) for c in text)

    with open(DECRYPTED_FILE, "w") as f:
        f.write(decrypted)


def verify_decryption():
    """
    Compares the original file and decrypted file
    to check whether decryption is successful.
    """
    if not os.path.exists(RAW_FILE) or not os.path.exists(DECRYPTED_FILE):
        return False

    with open(RAW_FILE, "r") as f1, open(DECRYPTED_FILE, "r") as f2:
        return f1.read().strip() == f2.read().strip()


# ---------------- MAIN PROGRAM ----------------
if __name__ == "__main__":
    """
    Takes user input for shift values,
    performs encryption and decryption,
    and verifies the final output.
    """
    try:
        s1 = int(input("Enter shift1: "))
        s2 = int(input("Enter shift2: "))

        encrypt_file(s1, s2)
        decrypt_file(s1, s2)

        if verify_decryption():
            print("\nDecryption successful!")
        else:
            print("\nDecryption failed")
            with open(RAW_FILE, "r") as f:
                print(f"Expected: {f.read().strip()}")
            with open(DECRYPTED_FILE, "r") as f:
                print(f"Got:      {f.read().strip()}")

    except ValueError:
        print("Please enter valid integers for the shifts.")
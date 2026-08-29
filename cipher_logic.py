"""
cipher_logic.py
Project 2: Basic Encryption & Decryption
"""

# Printable ASCII range: space (32) to '~' (126) = 95 characters total
PRINTABLE_START = 32
PRINTABLE_RANGE = 95


def encrypt(text, shift):
    """
    Encrypt text using Caesar Cipher logic.
    Shifts EVERY printable character the same way:
    letters, numbers, spaces, and punctuation are all encrypted.
    """
    result = ""
    for char in text:
        code = ord(char)
        if PRINTABLE_START <= code < PRINTABLE_START + PRINTABLE_RANGE:
            new_code = (code - PRINTABLE_START + shift) % PRINTABLE_RANGE + PRINTABLE_START
            result += chr(new_code)
        else:
            result += char
    return result


def decrypt(text, shift):
    """Decrypt text by reversing the Caesar Cipher shift."""
    return encrypt(text, -shift)


def normalize_shift(shift):
    """Safely wrap any shift value (negative or very large) into a valid range."""
    return shift % PRINTABLE_RANGE

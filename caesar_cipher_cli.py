"""
Project 2: Basic Encryption & Decryption
CLI Version
"""

from cipher_logic import encrypt, decrypt, normalize_shift


def main():
    print("=== Caesar Cipher: Encryption & Decryption Tool ===\n")

    message = input("Enter the text you want to encrypt: ")

    # Edge case: empty input
    if message.strip() == "":
        print("\nNo text entered. Nothing to encrypt.")
        return
    
    # Edge case: non-integer shift input
    while True:
        try:
            shift = int(input("Enter a shift key (e.g., 3): "))
            break
        except ValueError:
            print("Please enter a valid whole number.")

    # Edge case: extremely large/negative shifts are safely normalized
    shift = normalize_shift(shift)

    encrypted_text = encrypt(message, shift)
    decrypted_text = decrypt(encrypted_text, shift)

    print("\n--- Results ---")
    print(f"Original Text : {message}")
    print(f"Encrypted Text: {encrypted_text}")
    print(f"Decrypted Text: {decrypted_text}")


if __name__ == "__main__":
    main()

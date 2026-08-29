# Caesar Cipher: Encryption & Decryption Tool

A simple, extended implementation of the classic Caesar Cipher, built in Python with both a **command-line interface (CLI)** and a **graphical user interface (GUI)**.

Unlike a traditional Caesar Cipher (which only shifts letters), this version shifts **every printable ASCII character** — letters, numbers, spaces, and punctuation — giving it slightly stronger obfuscation while remaining easy to understand and reverse.

## Features

- 🔐 Encrypts and decrypts text using a Caesar Cipher shift
- 🔡 Covers the full printable ASCII range (32–126), not just A–Z
- 🖥️ Two ways to use it: a terminal-based CLI and a Tkinter-based GUI
- 🔁 Safe shift normalization — handles negative numbers and shifts larger than the character range without breaking
- ✅ Handles edge cases like empty input and non-numeric shift keys gracefully

## How It Works

The cipher shifts each character's position within the 95 printable ASCII characters (from space `' '` to tilde `'~'`) by a given key, wrapping around using modular arithmetic. Decryption simply reverses the shift.

```python
def encrypt(text, shift):
    ...
def decrypt(text, shift):
    return encrypt(text, -shift)
```

This logic lives in `cipher_logic.py` and is shared by both the CLI and GUI versions.

## Project Structure

```
decodes-cybersecurity-p2/
├── cipher_logic.py         # Core encryption/decryption logic
├── caesar_cipher_cli.py    # Command-line interface
├── caesar_cipher_gui.py    # Graphical interface (Tkinter)
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.14.4
- Tkinter (included with most standard Python installations; needed only for the GUI version)

### Installation

```bash
git clone https://github.com/Malaika-Murad/decodes-cybersecurity-p2.git
cd decodes-cybersecurity-p2
```

No external dependencies are required — everything uses Python's standard library.

## Usage

### CLI Version

Run the script and follow the prompts:

```bash
python caesar_cipher_cli.py
```

Example session:

```
=== Caesar Cipher: Encryption & Decryption Tool ===

Enter the text you want to encrypt: Hello, World!
Enter a shift key (e.g., 3): 3

--- Results ---
Original Text : Hello, World!
Encrypted Text: Khoor/#Zruog$
Decrypted Text: Hello, World!
```

### GUI Version

Launch the graphical tool:

```bash
python caesar_cipher_gui.py
```

1. Type or paste your text into the **input box**.
2. Enter a shift key (default is `3`).
3. Click **Encrypt** or **Decrypt** to see the result in the output box.

## Edge Cases Handled

- **Empty input** — the CLI exits early with a message instead of encrypting nothing.
- **Non-numeric shift values** — both the CLI and GUI prompt again / show an error instead of crashing.
- **Out-of-range shifts** (e.g., `1000` or `-50`) — automatically normalized using modulo arithmetic so the cipher always works correctly.

## Possible Future Improvements

- Add file-based encryption/decryption (encrypt entire `.txt` files)
- Add a "brute-force" mode to try all possible shifts on encrypted text
- Add copy-to-clipboard functionality in the GUI
- Package as a standalone executable

## Author

Built by [Malaika-Murad](https://github.com/Malaika-Murad) as part of a cybersecurity coursework project on basic encryption and decryption techniques.

## License

This project is currently unlicensed. Feel free to fork and adapt it for learning purposes.

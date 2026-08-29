"""
Project 2: Basic Encryption & Decryption
Caesar Cipher - GUI Version 
"""

import tkinter as tk
from tkinter import messagebox

from cipher_logic import encrypt, decrypt, normalize_shift


def run_encrypt():
    text = input_box.get("1.0", tk.END).rstrip("\n")
    try:
        shift = normalize_shift(int(shift_entry.get()))
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift key must be a whole number.")
        return
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, encrypt(text, shift))


def run_decrypt():
    text = input_box.get("1.0", tk.END).rstrip("\n")
    try:
        shift = normalize_shift(int(shift_entry.get()))
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift key must be a whole number.")
        return
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, decrypt(text, shift))


# ---- GUI Layout ----
window = tk.Tk()
window.title("Caesar Cipher Tool - DecodeLabs")
window.geometry("450x400")
window.resizable(False, False)

tk.Label(window, text="Enter Text:", font=("Arial", 11, "bold")).pack(pady=(10, 0))
input_box = tk.Text(window, height=5, width=50)
input_box.pack(pady=5)

tk.Label(window, text="Shift Key:", font=("Arial", 11, "bold")).pack(pady=(5, 0))
shift_entry = tk.Entry(window, width=10, justify="center")
shift_entry.insert(0, "3")
shift_entry.pack(pady=5)

btn_frame = tk.Frame(window)
btn_frame.pack(pady=10)
tk.Button(btn_frame, text="Encrypt", width=15, command=run_encrypt).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Decrypt", width=15, command=run_decrypt).grid(row=0, column=1, padx=5)

tk.Label(window, text="Output:", font=("Arial", 11, "bold")).pack(pady=(10, 0))
output_box = tk.Text(window, height=5, width=50)
output_box.pack(pady=5)

window.mainloop()

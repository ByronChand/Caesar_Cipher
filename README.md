# Caesar Cipher Project

This project implements a simple **Caesar Cipher**, which is a substitution cipher that shifts letters of the alphabet by a chosen amount.  
It supports:

- Encrypting text  
- Decrypting text  
- Validating shift values  

---

## Features

✔ Encrypt messages  
✔ Decrypt messages  
✔ Shift must be between 1 and 25  
✔ Preserves uppercase and lowercase  
✔ Ignores non-letter characters  
✔ Includes helper functions: `encrypt()` and `decrypt()`

## How to Run

### 1. Create and activate a virtual environment

**macOS / Linux**
python3 -m venv .venv
source .venv/bin/activate

**Windows**
python -m venv .venv
..venv\Scripts\Activate.ps1

---

### 2. Install dependencies

pip install -r requirements.txt

---

### 3. Run the program

python caesar.py

---

## Example Usage

### Encrypt:
encrypt("hello", 3)

→ "khoor"

### Decrypt:
decrypt("khoor", 3)

→ "hello"

---

## Project Structure

myproject/
├── caesar_cipher.py
├── README.md
├── requirements.txt
├── .gitignore
└── .venv/
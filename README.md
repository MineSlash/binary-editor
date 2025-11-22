<<<<<<< HEAD
# binary-editor
Binary file editor written in Python, supporting memory read/write.
=======
# Binary Editor (Python)

A lightweight and easy-to-use binary file editor written in pure Python.  
Supports reading, modifying, and saving `.bin` files with arbitrary memory addresses.

## ✨ Features

- Load and parse binary files
- In-memory memory editing
- Read arbitrary memory ranges in hex format
- Write and save modified binary files
- Tracks start address and memory length
- Handles integer or hex data input for writes

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/MineSlash/binary-editor.git
cd binary-editor
```

No external dependencies are required.

---

## 🔧 Usage Example

```python
from binary_editor import BinaryEditor

bin_editor = BinaryEditor('Sample.bin')

print("Start address:", bin_editor.start_address)
print("Length:", bin_editor.length)

# Read 16 bytes from 0x20
data = bin_editor.read('0x00000020', 0x10)
print("Read:", data)

# Write new data and save as a separate binary file
bin_editor.write(
    address='0x00000020',
    data='B0C1F0C1B0C1C1CADEADBEEF1EE7FEE7',
    output='Sample_modified.bin'
)
```

---

## 📂 Project Structure

```
binary-editor/
│
├─ binary_editor.py       # Main implementation
├─ Sample.bin             # Example binary file
├─ LICENSE                # MIT License
└─ README.md
```

---

## 🧠 How It Works

### Parsing
The `BinaryFile` class loads the binary file into a `bytearray`:
- Stores raw byte content in memory  
- Keeps track of the start address and file length  

### Memory Editing
The `BinaryEditor` wrapper provides:
- `read(address, length)` — read bytes in hex format  
- `write(address, data)` — write integer or hex data  
- Automatic handling of start address and length  
- Saving modified output back to `.bin`  

---

## 📝 License

This project is licensed under the **MIT License**.  
See the `LICENSE` file for details.

---

## 🤝 Contributing

Pull requests, enhancements, and bug reports are welcome.

---

## ⭐ Support

If you find this project useful, please consider giving it a star on GitHub! ⭐
>>>>>>> d984687 (Initial commit: Python Binary Editor and sample binary)

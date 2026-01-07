# 📦 Multi-Utility Toolkit (Python)

## 📌 Overview
This project is a **menu-driven Python application** that demonstrates the use of **modules and packages** in Python.
It combines multiple utilities into one program, helping beginners understand **real-world usage of Python standard libraries**.
---

## 🧩 Modules Used
The project uses the following built-in Python modules:

| Module | Purpose |
|------|--------|
| `datetime` | Work with dates and times |
| `time` | Stopwatch, delay, and countdown |
| `math` | Mathematical calculations |
| `random` | Random numbers, passwords, OTP |
| `string` | Character sets for passwords |
| `uuid` | Generate unique identifiers |
| `os` (implicit via file handling) | File operations |

---

## 🏗️ Project Structure

- `main()` → Main menu controller  
- `datetime_menu()` → Date & time utilities  
- `math_menu()` → Mathematical operations  
- `random_menu()` → Random data generation  
- `uuid_menu()` → UUID creation  
- `file_menu()` → File read/write/append  
- `explore_modules()` → Explore module attributes using `dir()`  

---

## ⏰ 1. Datetime and Time Operations
### Features:
- Show current date and time
- Calculate difference between two dates
- Format date using `ctime()`
- Stopwatch (start/stop)
- Countdown timer

### Concepts Used:
- `datetime.now()`
- `datetime.strptime()`
- `time.time()`
- `time.sleep()`
- `abs()` for positive difference

---

## ➕ 2. Mathematical Operations
### Features:
- Basic arithmetic (Add, Subtract, Multiply, Divide)
- Trigonometric functions (sin, cos, tan)
- Factorial calculation
- Logarithm with custom base
- Compound Interest calculation
- Geometric shapes (Area & Perimeter)

### Important Formulas:
- **Compound Interest**  
  `A = P (1 + r / (100n)) ^ (nt)`

- **Circle**
  - Area = πr²
  - Circumference = 2πr

---

## 🎲 3. Random Data Generation
### Features:
- Random number (1–100)
- Random password generator
- Random sample from user list
- OTP generation

### Concepts:
- `random.randint()`
- `random.choice()`
- `random.sample()`
- `string.ascii_letters`, `digits`, `punctuation`

---

## 🆔 4. UUID Generation
### Features:
- Generate single UUID
- Generate multiple UUIDs

### Concept:
- `uuid.uuid4()` generates a **globally unique identifier**

---

## 📁 5. File Operations
### Features:
- Write to a file
- Read from a file
- Append data to a file

### Modes Used:
- `'w'` → Write
- `'r'` → Read
- `'a'` → Append

Uses **context manager (`with open`)** for safety.

---

## 🔍 6. Explore Module Attributes
### Feature:
- View all methods and variables of any module

### Concept:
- `__import__()`
- `dir()`

Example:
```python
dir(math)
```

---

## ▶️ How to Run
```bash
python Moduler\ \&\ Packager.py
```
---

## 📚 Theory Section:

### 🔹 What is a Module in Python?
A **module** is a file that contains Python code such as:
- functions
- variables
- classes

Modules help us:
- reuse code
- organize large programs
- avoid writing the same code again

Examples used in this project:
- `math` → mathematical operations
- `datetime` → date and time handling
- `random` → random data generation

---

### 🔹 What is a Package?
A **package** is a collection of related modules stored in a directory.


### 🔹 Menu-Driven Program (Theory)
A **menu-driven program** allows the user to choose operations from a list.

Advantages:
- Easy to use
- User-friendly
- Suitable for large programs

This project uses:
- `while True` loop → to repeat menus
- `if-elif-else` → to handle choices

---

### 🔹 Exception Handling (Theory)
Exception handling prevents program crashes.

Used concept:
```python
try:
    ...
except ModuleNotFoundError:
    ...
```

Benefits:
- Handles errors safely
- Improves program reliability
- Provides meaningful error messages

---

### 🔹 File Handling Theory
File handling allows data to be stored permanently.

Modes used:
- `w` → Write (creates/overwrites file)
- `r` → Read file content
- `a` → Append data to file

Using `with open()`:
- Automatically closes the file
- Prevents data loss

---

### 🔹 UUID Theory
UUID stands for **Universally Unique Identifier**.

Characteristics:
- 128-bit unique value
- No duplication
- Used in databases, tokens, tracking IDs

Used function:
```python
uuid.uuid4()
```

---

### 🔹 Random Module Theory
The `random` module is used to generate unpredictable data.

Used functions:
- `randint()` → random numbers
- `choice()` → random element
- `sample()` → unique random selection

Applications:
- OTP generation
- Password creation
- Sampling data

---

### 🔹 Time & Datetime Theory
- `datetime` → works with real date and time
- `time` → delays, stopwatch, countdown

Important functions:
- `datetime.now()`
- `time.sleep()`
- `time.time()`



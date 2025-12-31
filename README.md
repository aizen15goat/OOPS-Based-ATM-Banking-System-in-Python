# OOPS-Based-ATM-Banking-System-in-Python

## 📌 Description
This project is a **console-based ATM banking system** developed in Python to demonstrate **core Object-Oriented Programming (OOPS) concepts** such as abstraction, inheritance, polymorphism, and encapsulation.

The system allows a user to select a bank, authenticate using a PIN, and perform banking operations like checking balance, withdrawing money, depositing money, and viewing transaction history.

---

## 🎯 Objectives
- Demonstrate real-world usage of **abstract base classes**
- Implement **runtime polymorphism** using a common ATM interface
- Practice clean OOPS design suitable for interviews and learning
- Simulate basic banking operations in a structured manner

---

## 🧠 OOPS Concepts Used

### 🔹 Abstraction
- `Bank` is an abstract base class
- It defines common operations like `withdraw()` and `deposit()`
- Concrete banks must implement these methods

### 🔹 Inheritance
- `SBI` and `HDFC` inherit from the `Bank` class
- Shared behavior is reused using `super()`

### 🔹 Polymorphism
- The `atm()` function works with any object of type `Bank`
- At runtime, the correct bank method is called automatically

### 🔹 Encapsulation
- PIN, balance, and transaction history are protected
- Access is provided only through class methods

---

## 🏗️ Class Structure


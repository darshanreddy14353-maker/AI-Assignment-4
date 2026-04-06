# AI Assignment 4 – CSP & Map Coloring 🧠

## 📌 Overview

This assignment focuses on solving **Constraint Satisfaction Problems (CSP)** using Python.
Each problem is modeled using variables, domains, and constraints, and solved using a **backtracking approach**.

---

## 📂 Problems Covered

* Map Coloring – Australia
* Map Coloring – Telangana (33 Districts)
* Sudoku Solver
* Cryptarithmetic Puzzle (SEND + MORE = MONEY)

---

## 🔹 1. Map Coloring – Australia

### 📖 Problem

Color the seven regions of Australia:

WA, NT, Q, SA, NSW, V, T

Such that no two adjacent regions share the same color.

### ⚙️ CSP Model

* Variables: Regions
* Domain: {Red, Green, Blue}
* Constraints: Adjacent regions must have different colors

### 🛠️ Approach

* Select an unassigned region
* Assign a valid color
* Check constraints with neighboring regions
* Backtrack if a conflict occurs

---

## 🔹 2. Map Coloring – Telangana

### 📖 Problem

Assign colors to 33 districts of Telangana ensuring that adjacent districts do not share the same color.

### ⚙️ CSP Model

* Variables: Districts
* Domain: {Red, Green, Blue, Yellow}
* Constraints: Neighboring districts must have different colors

### 🛠️ Approach

* Represent districts as a graph
* Apply backtracking search
* Assign colors while satisfying all constraints

---

## 🔹 3. Sudoku Solver

### 📖 Problem

Solve a 9×9 Sudoku puzzle such that:

* Each row contains digits 1–9 without repetition
* Each column contains digits 1–9 without repetition
* Each 3×3 subgrid contains digits 1–9 without repetition

### ⚙️ CSP Model

* Variables: 81 cells
* Domain: {1–9}
* Constraints: Row, column, and subgrid uniqueness

### 🛠️ Approach

* Identify empty cells
* Try numbers from 1 to 9
* Validate constraints
* Backtrack if needed

---

## 🔹 4. Cryptarithmetic Puzzle

### 📖 Problem

```
  SEND
+ MORE
-------
 MONEY
```

Each letter represents a unique digit.

### ⚙️ Constraints

* Each letter must map to a unique digit
* Leading digits cannot be zero
* The equation must be satisfied

### 🛠️ Approach

* Generate permutations of digits (0–9)
* Assign digits to letters
* Check if the equation is valid
* Stop when a valid solution is found

---

## ⚙️ Requirements

* Python 3.x
* No external libraries required

---

## ▶️ How to Run

```bash
python Australia_map.py
python Telangana_map.py
python Sudoku.py
python Cryptarithmetic.py
```

---

## 📊 Output

* Map Coloring → Color assignments for regions/districts
* Sudoku → Completed grid
* Cryptarithmetic → Valid equation output

---

## 🧠 Key Concepts

* Constraint Satisfaction Problems (CSP)
* Backtracking Algorithm
* Constraint Checking
* Graph Representation

---

## ✅ Conclusion

All problems are solved using CSP techniques with backtracking, ensuring that constraints are satisfied and valid solutions are obtained.

---

## 👨‍💻 Author

**G Chaitra Darshan Reddy**

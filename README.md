# Employee Management System

A beginner-friendly, object-oriented Python project to manage employees in a company. Supports full-time, part-time, and manager employees, with data persistence and a simple menu-driven interface.

---

## Table of Contents
- [Features](#features)
- [Object-Oriented Concepts](#object-oriented-concepts)
- [Class Structure](#class-structure)
- [How It Works](#how-it-works)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)

---

## Features
- Add, view, search, and remove employees
- Supports Full-Time, Part-Time, and Manager types
- Calculates total payroll and generates payroll reports
- Data is saved to a JSON file for persistence
- User-friendly, menu-driven interface

---

## Object-Oriented Concepts
- **Abstraction:** Abstract base class for Employee
- **Encapsulation:** Private variables and properties
- **Inheritance:** Specialized employee types inherit from Employee
- **Polymorphism:** Salary calculation differs by employee type
- **Composition:** Company class manages multiple Employee objects

---

## Class Structure

```mermaid
graph TD;
  Company --> Employee
  Employee <|-- FullTimeEmployee
  Employee <|-- PartTimeEmployee
  FullTimeEmployee <|-- Manager
```

- **Employee (Abstract):** ID, name, department, salary calculation (abstract)
- **FullTimeEmployee:** Fixed monthly salary
- **PartTimeEmployee:** Paid by the hour
- **Manager:** Full-time + bonus
- **Company:** Manages all employees, handles data persistence

---

## How It Works
1. **Start the program:**
   - Loads employee data from `employees.json` (if exists)
2. **Menu options:**
   - Add employee (choose type and enter details)
   - View all employees
   - Calculate total payroll
   - Search employee (by ID or name)
   - Remove employee
   - Generate payroll report
   - Exit
3. **Data persistence:**
   - All changes are saved automatically to `employees.json`

---

## Getting Started

### Prerequisites
- Python 3.x

### Running the Program
```bash
python employee_management.py
```

---

## Usage

Follow the on-screen menu to:
- Add Full-Time, Part-Time, or Manager employees
- View, search, or remove employees
- Calculate payroll and generate reports

### Example: Adding Employees
1. Choose `Add Employee`
2. Select type (Full-Time, Part-Time, Manager)
3. Enter details as prompted

### Example: Viewing Employees
- Choose `View All Employees` to see a list of all employees and their details

### Example: Calculating Payroll
- Choose `Calculate Total Payroll` to see the total salary for all employees

---

## Testing

### Example Employees
- **Full-Time:**
  - ID: E001, Name: John Smith, Dept: IT, Salary: $5000
- **Part-Time:**
  - ID: E002, Name: Sarah Johnson, Dept: Marketing, Rate: $15, Hours: 80
- **Manager:**
  - ID: E003, Name: Mike Wilson, Dept: Sales, Salary: $6000, Bonus: $1000

### Example Payroll Calculation
- John: $5000
- Sarah: $15 x 80 = $1200
- Mike: $6000 + $1000 = $7000
- **Total:** $13,200

### Data Persistence
- All employee data is saved in `employees.json` and loaded on startup.

---

## Troubleshooting
- "No existing employee data found" — Normal on first run
- "Employee with ID already exists" — Use unique IDs
- "Invalid amount entered" — Enter numbers for salary/rate/hours
- "Employee not found" — Check ID or name spelling
- File permission errors — Ensure write access to folder
- JSON file corruption — Delete `employees.json` and restart

---

## License
This project is for educational purposes and demonstrates OOP concepts in Python. 

# Employee Management System
# This program helps manage employees in a company
# Written by: [Student Name]
# Date: [Current Date]

import json
from abc import ABC, abstractmethod

# This is the main Employee class - all other employee types will inherit from this
class Employee(ABC):
    """This is the base class for all employees"""
    
    def __init__(self, employee_id, name, department):
        # These are private variables (using _ to show they are private)
        self._employee_id = employee_id
        self._name = name
        self._department = department
    
    # These are properties - they let us access private variables safely
    @property
    def employee_id(self):
        """Get the employee ID"""
        return self._employee_id
    
    @property
    def name(self):
        """Get the employee name"""
        return self._name
    
    @property
    def department(self):
        """Get the department"""
        return self._department
    
    @department.setter
    def department(self, new_department):
        """Set the department"""
        self._department = new_department
    
    # This is an abstract method - all child classes must implement this
    @abstractmethod
    def calculate_salary(self):
        """Calculate the salary - each employee type will do this differently"""
        pass
    
    def display_details(self):
        """Show basic employee information"""
        return f"ID: {self._employee_id}, Name: {self._name}, Dept: {self._department}"
    
    def to_dict(self):
        """Convert employee data to dictionary for saving to file"""
        return {
            'employee_id': self._employee_id,
            'name': self._name,
            'department': self._department
        }


# Full-time employees get a fixed monthly salary
class FullTimeEmployee(Employee):
    """This class represents full-time employees"""
    
    def __init__(self, employee_id, name, department, monthly_salary):
        # Call the parent class constructor first
        super().__init__(employee_id, name, department)
        self._monthly_salary = monthly_salary
    
    @property
    def monthly_salary(self):
        """Get the monthly salary"""
        return self._monthly_salary
    
    @monthly_salary.setter
    def monthly_salary(self, new_salary):
        """Set the monthly salary - make sure it's not negative"""
        if new_salary >= 0:
            self._monthly_salary = new_salary
        else:
            print("Salary cannot be negative!")
    
    def calculate_salary(self):
        """Calculate salary for full-time employee"""
        return self._monthly_salary
    
    def display_details(self):
        """Show full-time employee details"""
        basic_info = super().display_details()
        return f"{basic_info}, Monthly Salary: ${self._monthly_salary:.2f}"
    
    def to_dict(self):
        """Convert to dictionary for saving"""
        data = super().to_dict()
        data['monthly_salary'] = self._monthly_salary
        data['type'] = 'fulltime'
        return data


# Part-time employees get paid by the hour
class PartTimeEmployee(Employee):
    """This class represents part-time employees"""
    
    def __init__(self, employee_id, name, department, hourly_rate, hours_worked_per_month):
        # Call the parent class constructor first
        super().__init__(employee_id, name, department)
        self._hourly_rate = hourly_rate
        self._hours_worked_per_month = hours_worked_per_month
    
    @property
    def hourly_rate(self):
        """Get the hourly rate"""
        return self._hourly_rate
    
    @hourly_rate.setter
    def hourly_rate(self, new_rate):
        """Set the hourly rate - make sure it's not negative"""
        if new_rate >= 0:
            self._hourly_rate = new_rate
        else:
            print("Hourly rate cannot be negative!")
    
    @property
    def hours_worked_per_month(self):
        """Get the hours worked per month"""
        return self._hours_worked_per_month
    
    @hours_worked_per_month.setter
    def hours_worked_per_month(self, new_hours):
        """Set the hours worked - make sure it's not negative"""
        if new_hours >= 0:
            self._hours_worked_per_month = new_hours
        else:
            print("Hours worked cannot be negative!")
    
    def calculate_salary(self):
        """Calculate salary for part-time employee"""
        return self._hourly_rate * self._hours_worked_per_month
    
    def display_details(self):
        """Show part-time employee details"""
        basic_info = super().display_details()
        return f"{basic_info}, Hourly Rate: ${self._hourly_rate:.2f}, Hours: {self._hours_worked_per_month}"
    
    def to_dict(self):
        """Convert to dictionary for saving"""
        data = super().to_dict()
        data['hourly_rate'] = self._hourly_rate
        data['hours_worked_per_month'] = self._hours_worked_per_month
        data['type'] = 'parttime'
        return data


# Managers are full-time employees but get an extra bonus
class Manager(FullTimeEmployee):
    """This class represents managers - they inherit from FullTimeEmployee"""
    
    def __init__(self, employee_id, name, department, monthly_salary, bonus):
        # Call the parent class constructor first
        super().__init__(employee_id, name, department, monthly_salary)
        self._bonus = bonus
    
    @property
    def bonus(self):
        """Get the bonus amount"""
        return self._bonus
    
    @bonus.setter
    def bonus(self, new_bonus):
        """Set the bonus - make sure it's not negative"""
        if new_bonus >= 0:
            self._bonus = new_bonus
        else:
            print("Bonus cannot be negative!")
    
    def calculate_salary(self):
        """Calculate salary for manager (base salary + bonus)"""
        base_salary = super().calculate_salary()
        return base_salary + self._bonus
    
    def display_details(self):
        """Show manager details"""
        basic_info = super().display_details()
        return f"{basic_info}, Bonus: ${self._bonus:.2f}"
    
    def to_dict(self):
        """Convert to dictionary for saving"""
        data = super().to_dict()
        data['bonus'] = self._bonus
        data['type'] = 'manager'
        return data


# This is the main company class that manages all employees
class Company:
    """This class manages all employees in the company"""
    
    def __init__(self, data_file='employees.json'):
        # Dictionary to store all employees (ID -> Employee object)
        self._employees = {}
        # File name to save employee data
        self._data_file = data_file
        # Load existing data when we start
        self._load_data()
    
    def _load_data(self):
        """Load employee data from file"""
        try:
            with open(self._data_file, 'r') as file:
                data = json.load(file)
                
            # Go through each employee in the file
            for emp_data in data.values():
                emp_type = emp_data.get('type')
                
                # Create the right type of employee based on the 'type' field
                if emp_type == 'fulltime':
                    employee = FullTimeEmployee(
                        emp_data['employee_id'],
                        emp_data['name'],
                        emp_data['department'],
                        emp_data['monthly_salary']
                    )
                elif emp_type == 'parttime':
                    employee = PartTimeEmployee(
                        emp_data['employee_id'],
                        emp_data['name'],
                        emp_data['department'],
                        emp_data['hourly_rate'],
                        emp_data['hours_worked_per_month']
                    )
                elif emp_type == 'manager':
                    employee = Manager(
                        emp_data['employee_id'],
                        emp_data['name'],
                        emp_data['department'],
                        emp_data['monthly_salary'],
                        emp_data['bonus']
                    )
                
                # Add the employee to our dictionary
                self._employees[employee.employee_id] = employee
                
        except FileNotFoundError:
            # If file doesn't exist, that's okay - we start with no employees
            print("No existing employee data found. Starting fresh!")
        except Exception as e:
            print(f"Error loading data: {e}")
    
    def _save_data(self):
        """Save employee data to file"""
        try:
            # Convert all employees to dictionaries
            data = {}
            for emp_id, employee in self._employees.items():
                data[emp_id] = employee.to_dict()
            
            # Save to file
            with open(self._data_file, 'w') as file:
                json.dump(data, file, indent=2)
                
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def add_employee(self, employee):
        """Add a new employee to the company"""
        if employee.employee_id in self._employees:
            print(f"Employee with ID {employee.employee_id} already exists!")
            return False
        
        self._employees[employee.employee_id] = employee
        self._save_data()
        print(f"Employee {employee.name} added successfully!")
        return True
    
    def remove_employee(self, employee_id):
        """Remove an employee from the company"""
        if employee_id in self._employees:
            employee_name = self._employees[employee_id].name
            del self._employees[employee_id]
            self._save_data()
            print(f"Employee {employee_name} removed successfully!")
            return True
        else:
            print(f"Employee with ID {employee_id} not found!")
            return False
    
    def find_employee(self, employee_id):
        """Find an employee by ID"""
        return self._employees.get(employee_id)
    
    def calculate_total_payroll(self):
        """Calculate the total salary for all employees"""
        total = 0
        for employee in self._employees.values():
            total += employee.calculate_salary()
        return total
    
    def display_all_employees(self):
        """Show details of all employees"""
        if not self._employees:
            print("No employees found!")
            return
        
        print("\n=== ALL EMPLOYEES ===")
        for employee in self._employees.values():
            print(employee.display_details())
    
    def generate_payroll_report(self):
        """Generate a detailed payroll report"""
        if not self._employees:
            print("No employees found!")
            return
        
        print("\n=== PAYROLL REPORT ===")
        print("ID\t\tName\t\tType\t\tSalary")
        print("-" * 60)
        
        total_payroll = 0
        for employee in self._employees.values():
            salary = employee.calculate_salary()
            total_payroll += salary
            
            # Get employee type for display
            if isinstance(employee, Manager):
                emp_type = "Manager"
            elif isinstance(employee, FullTimeEmployee):
                emp_type = "Full-Time"
            else:
                emp_type = "Part-Time"
            
            print(f"{employee.employee_id}\t\t{employee.name}\t\t{emp_type}\t\t${salary:.2f}")
        
        print("-" * 60)
        print(f"TOTAL PAYROLL: ${total_payroll:.2f}")


# Main function to run the program
def main():
    """Main function to run the employee management system"""
    print("Welcome to Employee Management System!")
    print("=" * 40)
    
    # Create a company object
    company = Company()
    
    while True:
        # Show menu options
        print("\nWhat would you like to do?")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Calculate Total Payroll")
        print("4. Search Employee")
        print("5. Remove Employee")
        print("6. Generate Payroll Report")
        print("7. Exit")
        
        try:
            choice = input("\nEnter your choice (1-7): ")
            
            if choice == '1':
                # Add a new employee
                add_employee_menu(company)
                
            elif choice == '2':
                # View all employees
                company.display_all_employees()
                
            elif choice == '3':
                # Calculate total payroll
                total = company.calculate_total_payroll()
                print(f"\nTotal Payroll: ${total:.2f}")
                
            elif choice == '4':
                # Search for an employee
                search_employee(company)
                
            elif choice == '5':
                # Remove an employee
                remove_employee(company)
                
            elif choice == '6':
                # Generate payroll report
                company.generate_payroll_report()
                
            elif choice == '7':
                # Exit the program
                print("Thank you for using Employee Management System!")
                break
                
            else:
                print("Invalid choice! Please enter a number between 1 and 7.")
                
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")


def add_employee_menu(company):
    """Menu for adding different types of employees"""
    print("\nWhat type of employee do you want to add?")
    print("1. Full-Time Employee")
    print("2. Part-Time Employee")
    print("3. Manager")
    
    try:
        emp_type = input("Enter your choice (1-3): ")
        
        # Get common employee information
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        department = input("Enter Department: ")
        
        if emp_type == '1':
            # Add full-time employee
            try:
                monthly_salary = float(input("Enter Monthly Salary: $"))
                employee = FullTimeEmployee(emp_id, name, department, monthly_salary)
                company.add_employee(employee)
            except ValueError:
                print("Invalid salary amount!")
                
        elif emp_type == '2':
            # Add part-time employee
            try:
                hourly_rate = float(input("Enter Hourly Rate: $"))
                hours_worked = float(input("Enter Hours Worked per Month: "))
                employee = PartTimeEmployee(emp_id, name, department, hourly_rate, hours_worked)
                company.add_employee(employee)
            except ValueError:
                print("Invalid amount entered!")
                
        elif emp_type == '3':
            # Add manager
            try:
                monthly_salary = float(input("Enter Monthly Salary: $"))
                bonus = float(input("Enter Monthly Bonus: $"))
                employee = Manager(emp_id, name, department, monthly_salary, bonus)
                company.add_employee(employee)
            except ValueError:
                print("Invalid amount entered!")
                
        else:
            print("Invalid choice!")
            
    except Exception as e:
        print(f"Error adding employee: {e}")


def search_employee(company):
    """Search for an employee by ID or name"""
    print("\nSearch by:")
    print("1. Employee ID")
    print("2. Employee Name")
    
    try:
        search_choice = input("Enter your choice (1-2): ")
        
        if search_choice == '1':
            # Search by ID
            emp_id = input("Enter Employee ID: ")
            employee = company.find_employee(emp_id)
            
            if employee:
                print(f"\nFound Employee:")
                print(employee.display_details())
            else:
                print("Employee not found!")
                
        elif search_choice == '2':
            # Search by name
            search_name = input("Enter Employee Name: ").lower()
            found = False
            
            for employee in company._employees.values():
                if search_name in employee.name.lower():
                    print(f"\nFound Employee:")
                    print(employee.display_details())
                    found = True
            
            if not found:
                print("No employees found with that name!")
                
        else:
            print("Invalid choice!")
            
    except Exception as e:
        print(f"Error searching: {e}")


def remove_employee(company):
    """Remove an employee by ID"""
    try:
        emp_id = input("Enter Employee ID to remove: ")
        company.remove_employee(emp_id)
    except Exception as e:
        print(f"Error removing employee: {e}")


# Run the program if this file is executed directly
if __name__ == "__main__":
    main() 
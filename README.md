# Alt-school-Fall-Semester-DE-Exams-Hands-on-Project-2023

# <center>Expense Management System </center>

## Introduction
This Python project consists of two classes, `Expense` and `ExpenseDatabase`, that enable the management of financial expenses.

## Usage
To use this code:
 - Clone the repository to your local machine using the following command:
   ```bash
   git clone https://github.com/bideeen/Alt-school-Fall-Semester-DE-Exams-Hands-on-Project-2023.git

## Running the Code:
 - Ensure you have Python installed on your system.
 - Open a terminal or command prompt.
 - Run the test script by executing:
  ```bash
  python test_expense_app.py
  ```

# Example Usage
The test_expense_app.py script demonstrates the functionality of the Expense and ExpenseDatabase classes. Below is an example of how you can use these classes in your own code:
```python
from expenseApp import Expense, ExpenseDatabase

# Create instances of Expense and ExpenseDatabase classes
expense1 = Expense("Groceries", 50.00)
expense2 = Expense("Dinner", 75.00)

# Initialize an ExpenseDatabase instance
expense_db = ExpenseDatabase()

# Add expenses to the database
expense_db.add_expense(expense1)
expense_db.add_expense(expense2)

# Retrieve an expense by ID
retrieved_expense = expense_db.get_expense_by_id(expense1.id)

# Print the retrieved expense as a dictionary
print(retrieved_expense.to_dict())  
```


**Note**: ***Feel free to modify, run, and extend the code as needed!***


<br/>

# Thank You
# 
import uuid
from datetime import datetime



# The Expense Class
class Expense:
    # Initialize expense attributes
    def __init__(self, title, amount):
        # Generate a unique ID for the expense
        self.id =  str(uuid.uuid4())
        self.title = title
        self.amount = amount
        
        # Record creation time
        self.created_at = datetime.utcnow()
        # Initially set updated time to creation time
        self.updated_at = self.created_at       

    # Update expense details and timestamp
    def update(self, title=None, amount=None):
        if title:
            self.title = title
        if amount:
            self.amount = amount
        
        # Update timestamp
        self.updated_at = datetime.utcnow()
        
    # A function to return expense details as a dictionary
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'amount': self.amount,
            'created_at': self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            'updated_at': self.updated_at.strftime("%Y-%m-%d %H:%M:%S")
        }



# Expenses Database Class
class ExpenseDatabase:
    # Initialize an empty list to store expenses
    def __init__(self):
        self.expenses = []
        
    # Add expense to the database
    def add_expense(self, expense):
        self.expenses.append(expense)
        
    # Remove expense from the database by ID
    def remove_expense(self, expense_id):
        self.expenses = [expense for expense in self.expenses if expense.id != expense_id]
        
    # Get an expense from the database by ID
    def get_expense_by_id(self, expense_id):
        for expense in self.expenses:
            if expense.id == expense_id:
                return expense
        return None
        
    # Get expenses from the database by title
    def get_expenses_by_title(self, title):
        return [expense for expense in self.expenses if expense.title == title]

    # A function to return a list of dictionaries representing expenses in the database
    def to_dict(self):
        return [expense.to_dict() for expense in self.expenses]
        

        
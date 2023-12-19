from expenseApp import Expense, ExpenseDatabase

def get_expenses():

    # Create instances of Expense
    expense1 = Expense("Groceries", 50.00)
    expense2 = Expense("Dinner", 75.00)

    # Initialize an ExpenseDatabase instance
    expense_db = ExpenseDatabase()

    # Add expenses to the database
    expense_db.add_expense(expense1)
    expense_db.add_expense(expense2)

    # Retrieve an expense by ID
    retrieved_expense = expense_db.get_expense_by_id(expense1.id)
    print("Retrieved Expense:")
    print(retrieved_expense.to_dict())  # Print the retrieved expense as a dictionary

    # Update an expense
    expense_db.get_expense_by_id(expense2.id).update(title="Restaurant", amount=100.00)

    return expense_db

if __name__ == '__main__':

    # Get all expenses
    all_expenses = get_expenses().to_dict()
    print("\nAll Expenses:")
    for exp in all_expenses:
        print(exp)

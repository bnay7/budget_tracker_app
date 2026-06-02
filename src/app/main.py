from . import database
from . models import Transcation


def display_menu():
    """Displays the main menyu to the user"""
    print("\n----------Budget Tracker Menu--------")
    print("1. Add Revenue")
    print("2. Add Expenses")
    print("3. View All Transcations")
    print("4. View Balance")
    print("5. Exit")
    print("-------------------")


def get_transcation_details(type):
    """Gets description and amount input from the user."""
    while True:
        description = input(f"Enter the {type} description: ")
        if description:
            break
        else:
            print("Description cannot be empty")

    while True:
        try:
            amount_str = input(f"Enter {type} amount: ")
            amount = float(amount_str)
            if amount >= 0:
                return description, amount
            else:
                print("Amount cannot be non negative")
        except ValueError:
            print("Invalis amount. Please enter a number")


def add_revenue():
    """Add the revenue"""
    print("\n------------------")
    description, amount = get_transcation_details('revenue')
    transcation = Transcation(
        type='revenue', description=description, amount=amount)
    database.add_transcation(transcation)


def add_expense():
    """Add the expenses"""
    print("\n------------------")
    description, amount = get_transcation_details('expense')
    transcation = Transcation(
        type='expense', description=description, amount=amount)
    database.add_transcation(transcation)


def view_transcation():
    """"View all the transcation"""
    print("\n------------------")
    transcation = database.get_all_transactions()
    if not transcation:
        print("No transcations exits yet")
        return
    for tran in transcation:
        print(tran.display())
    print("\n------------------")


def view_balance():
    """Calculate and displays the current balance."""
    print("\n------------------")
    transaction = database.get_all_transactions()
    total_revenue = sum(
        tran.amount for tran in transaction if tran.type == 'revenue')
    total_expenses = sum(
        tran.amount for tran in transaction if tran.type == 'expense')
    balance = total_revenue - total_expenses

    print(f"Total Revenue: +{total_revenue:.2f}")
    print(f"Total Expenses: +{total_expenses:.2f}")
    print("------------------")
    print(f"Current Balance: {balance:.2f}")
    print("------------------")


def run_app():
    """Main application loop."""
    while True:
        display_menu()
        choice = input("Enter you operation (1-5): ")
        if choice == '1':
            add_revenue()
        elif choice == '2':
            add_expense()
        elif choice == '3':
            view_transcation()
        elif choice == '4':
            view_balance()
        elif choice == '5':
            print("Exiting program")
            break
        else:
            print("Invalid choice. Please enter option 1- 5")

        input("\n Press Enter to continue.. ")

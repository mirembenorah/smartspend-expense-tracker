
# SmartSpend Expense Tracker
# A simple program for recording and tracking expenses

expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    print("Expense added successfully!")

def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n--- Your Expenses ---")
    for expense in expenses:
        print(
            f"Name: {expense['name']} | "
            f"Amount: UGX {expense['amount']:,.0f} | "
            f"Category: {expense['category']}"
        )

def show_total():
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total spending: UGX {total:,.0f}")

def main():
    while True:
        print("\n===== SMARTSPEND =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Spending")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            print("Thank you for using SmartSpend!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

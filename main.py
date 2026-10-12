expenses = []

while True:
    print("Personal Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        category = input("Enter expense category: ")

        try:
            amount = float(input("Enter amount in Rs: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            expenses.append({
                "category": category,
                "amount": amount
            })

            print("Expense added successfully!")

        except ValueError:
            print("Please enter a valid number.")

    elif choice == "2":
        if not expenses:
            print("No expenses recorded yet.")
        else:
            for expense in expenses:
                print(
                    expense["category"],
                    "- Rs",
                    expense["amount"]
                )

    elif choice == "3":
        total = sum(
            expense["amount"]
            for expense in expenses
        )

        print("Total expenses: Rs", round(total, 2))

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")
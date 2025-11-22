expense_records = []
category_totals = {}
unique_categories = set()

print ("Personal Expense Manager 2025")

ans=True
while ans:
    print("\nExpense Tracker Menu:")
    print("1. Enter New Expenses")
    print("2. View My Overall Spending Report")
    print("3. View Spending Categories")
    print("4. View Spending By Category")
    print("5. Exit")

    ans=input("Enter your choice: ")

    if ans == '1':
        for i in range (1,6):
            category = input(f"Enter Expense {i} category ")
            amount = float(input(f"Enter Expense {i} amount "))
            date = input(f"Enter Expense {i} date (YYYY-MM-DD) ")
            expense_records.append([category, amount, date])

        for category, amount, date in expense_records:
            unique_categories.add(category)
            category_totals[category] = category_totals.get(category, 0) + amount

    if ans == '2':
        all_amounts = [amount for category, amount, date in expense_records]
        total_spending = sum(all_amounts)
        average_expense = total_spending / len(expense_records)
        highest_expense = max(all_amounts) if all_amounts else 0
        lowest_expense = min(all_amounts) if all_amounts else 0

        highest_expense_record = max(expense_records, key=lambda x: x[1]) if expense_records else None
        lowest_expense_record = min(expense_records, key=lambda x: x[1]) if expense_records else None
        print ("===OVERALL SPENDING SUMMARY===")
        print (f'Total Spending: ${total_spending}')
        print (f'Average Expense: ${average_expense}')
        print (f'Highest Expense: ${highest_expense}')
        print (f'Lowest Expense: ${lowest_expense}')

    if ans == '3':
       print(f'===UNIQUE SPENDING CATEGORIES===')
       print(f'Unique Categories Spent on: {list(unique_categories)}')

    if ans == '4':
       print('===SPENDING BY CATEGORY===')
       for category, total in category_totals.items():
           print(f'Category: {category}, Total: ${total}')

    elif ans == '5':
        print("\nExiting...")
        break

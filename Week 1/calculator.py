#This is a simple program to produce a business calculator
#We will start by greeting the user and request they provide us with their monthly revenue data
print("Welcome to Business Calculator 2025")
print("Please have your monthly Revenue and Expenses data ready to input")
print("First, please enter revenue for each month of the financial year")

#Get business revenue from user
#We do this by defining the 'revenue' variable as whatever the user 'inputs'
#The input must be a real number with decimal points, with the function 'float'
#User inputs revenue for each month
revenuejan = float(input("Enter January Revenue: $"))
revenuefeb = float(input("Enter February Revenue: $"))
revenuemar = float(input("Enter March Revenue: $"))
revenueapr = float(input("Enter April Revenue: $"))
revenuemay = float(input("Enter May Revenue: $"))
revenuejun = float(input("Enter June Revenue: $"))
revenuejul = float(input("Enter July Revenue: $"))
revenueaug = float(input("Enter August Revenue: $"))
revenuesep = float(input("Enter September Revenue: $"))
revenueoct = float(input("Enter October Revenue: $"))
revenuenov = float(input("Enter November Revenue: $"))
revenuedec = float(input("Enter December Revenue: $"))

#After entering this data, we thank the user and request that they now provide all expenses information
print("Thank you. Now, please enter expenses for each month of the financial year")

#The calculator will then sum all above monthly revenue inputs from the user, and uses this sum
#to define the 'revenuetotal' variable
#Also defines average monthly revenue by dividing 'revenuetotal' by the number of entries, 12
revenue_total = revenuejan + revenuefeb + revenuemar + revenueapr + revenuemay + revenuejun + revenuejul + revenueaug + revenuesep + revenueoct + revenuenov + revenuedec
revenue_ave = revenue_total / 12

#Get business costs from user
#As above, but defining the new variable 'cost' instead based on user input
costjan = float(input("Enter January Expenses: $"))
costfeb = float(input("Enter February Expenses: $"))
costmar = float(input("Enter March Expenses: $"))
costapr = float(input("Enter April Expenses: $"))
costmay = float(input("Enter May Expenses: $"))
costjun = float(input("Enter June Expenses: $"))
costjul = float(input("Enter July Expenses: $"))
costaug = float(input("Enter August Expenses: $"))
costsep = float(input("Enter September Expenses: $"))
costoct = float(input("Enter October Expenses: $"))
costnov = float(input("Enter November Expenses: $"))
costdec = float(input("Enter December Expenses: $"))

#The calculator will then sum all above monthly cost inputs from the user to define cost_total and the cost_ave, 
#as above like for revenue
cost_total = costjan + costfeb + costmar + costapr + costmay + costjun + costjul + costaug + costsep + costoct + costnov + costdec
cost_ave = cost_total / 12

#Calculate profits
#Now that the user has defined both the 'revenue' and 'cost' variables, we make the program
#run a simply calculation to define the new variable 'profit'
profit = revenue_total - cost_total

#We now define the margin variable as the profit margin, by converting the profit value into a percentage 
margin = (profit/revenue_total) * 100

#We then display the values of all four of these variables for the user, by printing f-strings
print("\n--- Financial Summary ---")
print(f"Total Revenue: ${revenue_total:,.2f}")
print(f"Average Monthly Revenue: ${revenue_ave:,.2f}")
print(f"Total Expenses: ${cost_total:,.2f}")
print(f"Average Monthly Expenses: ${cost_ave:,.2f}")
print(f"Total Annual Profit: ${profit:,.2f}")
print(f"Annual Profit Margin: {margin:,.2f}%")

#We then also rank the user's profit margins based on an arbitrary ranking system, and then
#display the ranking notice with the print function
if margin >=50:
    print("Annual Profit Margins are Great") 
elif margin >= 20:
    print("Annual Profit Margins are Average")
else: print("Annual Profit Margins are Poor")
'''1. Write a Python script that asks the user for their monthly income and monthly expenses.
2. Calculate their monthly savings and determine if they are saving enough:
● If savings are greater than 20% of their income, print: “You are saving enough!”
● If not, print: “You need to save more.”
3. Include the following:
● Use arithmetic operators for calculations (e.g., income - expenses).
● Use comparison operators (e.g., savings > 0.2 * income).
● Use logical operators to check multiple conditions (e.g., and, or).
4. Save the final script as savings_calculator.py.'''


income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your monthly expenses: "))
savings = income - expenses
saving_persentage = (savings / income) * 100
if savings > income*0.2:
    print("You are saving enough!", saving_persentage, "% which is more than 20% of your income.")
else:
    print("You need to save more.", saving_persentage, "as you savings is less than 20% of your income.")
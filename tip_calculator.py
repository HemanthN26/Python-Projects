print("Welcome to Tip Calculator")
total_bill = input("What was the total bill?\n")
tip = input("How much tip would you like to give? 10, 12 or 15\n")
people = input("How many of you are spliting the bill?\n")
cal = int(total_bill) + int(tip) / int(people)
print(f"each person should pay {cal}")



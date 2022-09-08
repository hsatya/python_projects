print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? Rs."))
no_of_people = int(input("How many people to split the bill? "))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
total_amount_to_pay = total_bill + (total_bill * (tip_percentage / 100));
amount_per_person = round(total_amount_to_pay / no_of_people);

print(f"Each person should pay: Rs.{amount_per_person}")
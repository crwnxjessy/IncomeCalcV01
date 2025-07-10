print("Income Calculator by Jessy")

nwc = float(input("What is your hourly pay? $"))
hpd = float(input("How many hours do you work per day? "))
dpw = float(input("How many days do you work per week? "))

weekly_hours = hpd * dpw
weekly_pay = nwc * weekly_hours

monthly_pay = weekly_pay * 5

print(f"Your total hours worked per week: {weekly_hours} hours")
print(f"Your weekly pay is: ${weekly_pay:.2f}")
print(f"Your estimated monthly pay is: ${monthly_pay:.2f}")

ppm = float(input("Want to know per month? Enter how many months to calculate: "))

yearly_pay = monthly_pay * ppm

print(f"You're estimated pay for", ppm, " months is", yearly_pay)
print("Thank you for trying this calculator out!")

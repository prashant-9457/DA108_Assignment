# Calculator for Birthday countdown

from datetime import date

# Step 1: Get user input
year = int(input("Enter your birth year: "))
month = int(input("Enter your birth month: "))
day = int(input("Enter your birth day: "))

# Step 2: Get today's date
today = date.today()

# Step 3: Create birthdate object
birthdate = date(year, month, day)

# Step 4: Calculate age
age = today.year - birthdate.year
if (today.month, today.day) < (birthdate.month, birthdate.day):
    age -= 1

print(f"You are {age} years old.")

# Step 5: Determine next birthday
this_year_birthday = date(today.year, month, day)

if this_year_birthday < today:
    next_birthday = date(today.year + 1, month, day)
else:
    next_birthday = this_year_birthday

# Step 6: Countdown to next birthday
countdown = (next_birthday - today).days
print(f"Your next birthday is in {countdown} days.")

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
days =  (90*365)-int(age) * 365
weeks = (90*52) - int(age) * 52
months = (90*12) - int(age) * 12

print(f"You have {int(days)} days, {int(weeks)} weeks, and {int(months)} months left.")


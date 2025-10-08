# Author: Aayan Srivastwa
# Date: 08-10-2025
# Daily Calorie Tracker - Simple & Easy to Understand Version
# This program helps users track their daily calorie intake by logging meals and their calorie counts.

# Task 1: Welcome Message

print("===================================")
print(" Welcome to the Daily Calorie Tracker by Aayan Srivastwa")
print("===================================\n")

# Task 2: Input & Store Data    

meals = []
calories = []
num_meals = int(input("How many meals did you have today? "))


for i in range(num_meals):
    meal_name = input(f"\nEnter the name of meal {i+1}: ")
    cal_amount = int(input(f"Enter calories for {meal_name}: "))

    
    meals.append(meal_name)
    calories.append(cal_amount)

# Task 3: Calorie calculations

totalcalories = sum(calories)
averagecalories = totalcalories / len(calories)
daily_limit = int(input("\nWhat is your daily calorie limit? "))

# Task 4: Limit exceeding Warning system

if total_calories > daily_limit:
    print("\n WARNING: You ate more than your daily calorie limit!")
else:
    print("\n Great job! You are within your daily calorie goal.")
print("\n========== Your Daily Summary ==========")
print("Meal Name\Calories")
print("----------------------------------------")

# Task 5: Formatted outputs using \t and \n

for i in range(len(meals)):
    print(f"{meals[i]}\t\t{calories[i]}")

print("----------------------------------------")
print(f"Total Calories:\t{total_calories}")
print(f"Average Calories:\t{average_calories:.2f}")

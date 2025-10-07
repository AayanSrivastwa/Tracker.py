# tracker.py
# Author: Aayan Srivastwa
# Date: 09-10-2025
# Project: Daily Calorie Tracker CLI Tool# Project: Daily Calorie Tracker CLI Tool


print("Welcome to the Daily Calorie Tracker! ")
print("This tool helps you log your meals, track total calorie intake,")
print("compare it against your daily limit, and save session logs.\n")
meals = []
calories = []
num_meals = int(input("How many meal you took today? "))

for i in range(num_meals):
    meal_name = input(f"Enter meal {i+1} name: ")
    calorie_amount = float(input(f"Enter calories for {meal_name}: "))

    meals.append(meal_name)
    calories.append(calorie_amount)

total_calories = sum(calories)
average_calories = total_calories / len(calories)

daily_limit = float(input("\nEnter your daily calorie limit: "))

print("\n Daily Summary ")
print("Meal Name\tCalories")
print("-------------------------------------")

for meal, cal in zip(meals, calories):
    print(f"{meal}\t\t{cal}")

print("-------------------------------------")
print(f"Total:\t\t{total_calories}")
print(f"Average:\t{average_calories:.2f}")

if total_calories > daily_limit:
    print("⚠️ Warning: You have exceeded your daily calorie limit!")
else:
    print("✅ Good job! You are within your daily calorie limit.")

# ================= Save Session Log =================
save_option = input("\nDo you want to save this session? (Y/N):")

if save_option == "yes":
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = "calorie_log.txt"

    with open(filename, "w") as file:
        file.write(f"Daily Calorie Tracker Log - {timestamp}\n")
        file.write("=====================================\n")
        for meal, cal in zip(meals, calories):
            file.write(f"{meal}: {cal} cal\n")
        file.write("-------------------------------------\n")
        file.write(f"Total: {total_calories} cal\n")
        file.write(f"Average: {average_calories:.2f} cal\n")
        file.write(f"Daily Limit: {daily_limit} cal\n")
        if total_calories > daily_limit:
            file.write("Status: Exceeded limit ⚠️\n")
        else:
            file.write("Status: Within limit ✅\n")

    print(f"✅ Session saved to {filename}")

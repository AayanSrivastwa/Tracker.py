# Tracker.py

🥗 Daily Calorie Tracker CLI
📘 Overview

A simple Command-Line Interface (CLI) tool built in Python to help users log their meals, calculate total and average calorie intake, compare against a user-defined daily limit, and optionally save the session as a report file.
This mini project was created for the course: Programming for Problem Solving using Python.

🧩 Project Description

tracker.py is a lightweight Python script that:

Prompts the user for a daily calorie limit

Collects meal names and calorie values

Computes total and average calories

Warns if the limit is exceeded

Displays a formatted summary table

Optionally saves the session log to calorie_log.txt

🎯 Learning Objectives Covered

| **Objective**              | **How Addressed**                            |
| -------------------------- | -------------------------------------------- |
| `input()`, type conversion | Used for numeric (float/int) and text inputs |
| Lists & data storage       | Parallel lists: `meal_names`, `calorie_val`  |
| Arithmetic & comparison    | Total, average, limit comparison, warning    |
| String formatting          | f-strings, `\n`, `\t`, decorative lines      |
| File I/O                   | Writes structured log with timestamp         |
| Logical thinking           | Structured task flow (Tasks 1–6)             |


⚙️ Program Flow (Task Mapping)
| **Task**       | **Implementation in tracker.py**                     |
| -------------- | ---------------------------------------------------- |
| Task 1         | Header comments + welcome prints                     |
| Task 2         | Loop over user-specified meal count; append to lists |
| Task 3         | Use `sum()` for total; compute average               |
| Task 4         | If total exceeds daily limit → show warning          |
| Task 5         | Display formatted table with tabs and lines          |
| Task 6 (Bonus) | Optional save with timestamp using `datetime`        |



💻 Sample Run (Example 1)
--- Daily Calorie Tracker CLI by Aayan Srivastwa ---

Enter your daily calorie limit: 2000
How many meals do you want to enter: 3

Meal 1:
Meal name: Vada Pav
Calories for Vada Pav: 600

Meal 2:
Meal name: Patato
Calories for Potato: 700

Meal 3:
Meal name: Icecream
Calories for Icecream: 800

Meal Name                  Calories:
--------------------------------------------------
Vada Pao                  600.0 cal
Potato                    700.0 cal
Icecream                  800.0 cal

Total calories: 2100.0
Average calories: 700.0
⚠️ WARNING: Daily calorie limit exceeded!


💻 Sample Run (Example 2)

--- Daily Calorie Tracker CLI by Aayan Srivastwa ---

Enter your daily calorie limit: 2000
How many meals do you want to enter: 3

Meal 1:
Meal name: Apple
Calories for Apple: 600

Meal 2:
Meal name: Banana
Calories for Banana: 700

Meal 3:
Meal name: Kiwi
Calories for Kiwi: 800

Meal Name                  Calories:
--------------------------------------------------
Apple                      600.0 cal
Banana                     700.0 cal
Kiwi                       800.0 cal

Total calories: 2100.0
Average calories: 700.0
⚠️ WARNING: Daily calorie limit exceeded!

💻 Sample Run (Example 3)
--- Daily Calorie Tracker CLI by Aayan Srivastwa ---

Enter your daily calorie limit: 2000
How many meals do you want to enter: 3

Meal 1:
Meal name: Golgappe
Calories for Golgappe: 600

Meal 2:
Meal name: Paratha
Calories for Paratha : 700

Meal 3:
Meal name: Chicken Tikka
Calories for Chicken Tikka: 800

Meal Name                  Calories:
--------------------------------------------------
Golgappe                   600.0 cal
Paratha                    700.0 cal
Chicken Tikka              800.0 cal

Total calories: 2100.0
Average calories: 700.0
⚠️ WARNING: Daily calorie limit exceeded!




This project demonstrates the application of basic Python programming concepts such as user input, loops, arithmetic operations, conditional logic, string formatting, and file handling to solve a real-world problem in a structured and user-friendly way.



Details
Aayan Srivastwa
2501410049
B.Tech CSE Cyber Security(1st Semester)
9th October 2025
Programming With Python - Lab Assignment 1

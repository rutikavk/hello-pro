name = input("Enter your name: ")
daily_goal = input("Enter your daily goal: ")

with open("journal.txt", "a") as file:
    entry = f"Name: {name}\nDaily Goal: {daily_goal}\n{'-' * 30}\n"
    file.write(entry)
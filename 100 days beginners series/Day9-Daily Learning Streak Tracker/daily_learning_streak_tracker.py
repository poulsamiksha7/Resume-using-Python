from datetime import datetime, timedelta

today = datetime.now().date()
answer = input("Did you learn today? (yes/no): ").lower()

try:
    with open("streak.txt", "r") as file:
        last_date_str = file.readline().strip()
        streak = int(file.readline().strip())
        last_date = datetime.strptime(last_date_str, "%Y-%m-%d").date()
except:
    last_date = None
    streak = 0

if last_date == today:
    print(f"You already recorded today. Current streak: {streak} days")

else:
    if last_date == today - timedelta(days=1):
        if answer == "yes":
            streak += 1
        else:
            streak = 0
    else:
        if answer == "yes":
            streak = 1
        else:
            streak = 0

    with open("streak.txt", "w") as file:
        file.write(f"{today}\n")
        file.write(f"{streak}\n")

    print(f"Current learning streak: {streak} days")

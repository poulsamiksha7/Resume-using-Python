positive = 0
negative = 0

print("Answer with yes or no\n")

good_mood = input("Did you feel good most of the day? ").lower()
if good_mood == "yes":
    positive += 1
else:
    negative += 1

productive = input("Were you productive today? ").lower()
if productive == "yes":
    positive += 1
else:
    negative += 1

stress = input("Did you feel stressed today? ").lower()
if stress == "yes":
    negative += 1
else:
    positive += 1

rest = input("Did you get enough rest today? ").lower()
if rest == "yes":
    positive += 1
else:
    negative += 1

print("\nDay Analysis:")

if positive > negative:
    print("Overall, you had a good day 😊")
elif negative > positive:
    print("Today was a tough day. Be kind to yourself 💙")
else:
    print("Your day was balanced. Some ups, some downs.")

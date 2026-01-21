score = 0

print("Answer with yes or no\n")

sleep = input("Did you get enough sleep? ").lower()
if sleep == "yes":
    score += 2

boundaries = input("Did you respect your boundaries today? ").lower()
if boundaries == "yes":
    score += 2

work = input("Did you do at least one important task? ").lower()
if work == "yes":
    score += 2

self_talk = input("Did you speak kindly to yourself? ").lower()
if self_talk == "yes":
    score += 2

care = input("Did you take care of your body or mind today? ").lower()
if care == "yes":
    score += 2

print("\nYour Self-Respect Score:", score, "/ 10")

if score <= 3:
    print("Low self-respect today. Be gentle — tomorrow is a new chance.")
elif 4 <= score <= 7:
    print("Moderate self-respect. You’re trying, and that matters.")
else:
    print("High self-respect! You showed up for yourself today 💙")

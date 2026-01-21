introvert_score = 0
extrovert_score = 0

print("Answer with A or B\n")


q1 = input("1. After social gatherings, you feel:\nA) Energized\nB) Drained\n> ").lower()
if q1 == "a":
    extrovert_score += 1
elif q1 == "b":
    introvert_score += 1

q2 = input("\n2. Your ideal weekend looks like:\nA) Going out with friends\nB) Staying home alone\n> ").lower()
if q2 == "a":
    extrovert_score += 1
elif q2 == "b":
    introvert_score += 1


q3 = input("\n3. In group discussions, you usually:\nA) Speak easily\nB) Listen more\n> ").lower()
if q3 == "a":
    extrovert_score += 1
elif q3 == "b":
    introvert_score += 1

print("\nResult:")
if extrovert_score > introvert_score:
    print("You show more extroverted tendencies.")
elif introvert_score > extrovert_score:
    print("You show more introverted tendencies.")
else:
    print("You show a balance of introverted and extroverted traits (Ambivert).")

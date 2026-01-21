reward = 0
fear = 0
growth = 0

print("Answer with A, B, or C\n")

# Question 1
q1 = input("1. What usually pushes you to start a task?\n"
           "A) The reward or result at the end\n"
           "B) Fear of missing a deadline or failing\n"
           "C) Desire to improve or learn\n> ").lower()

if q1 == "a":
    reward += 1
elif q1 == "b":
    fear += 1
elif q1 == "c":
    growth += 1

# Question 2
q2 = input("\n2. When you succeed, what feels best?\n"
           "A) Recognition or achievement\n"
           "B) Relief that it’s over\n"
           "C) What you learned from it\n> ").lower()

if q2 == "a":
    reward += 1
elif q2 == "b":
    fear += 1
elif q2 == "c":
    growth += 1

q3 = input("\n3. When things get difficult, you continue because:\n"
           "A) You want the outcome\n"
           "B) You don’t want to fail\n"
           "C) You want to grow stronger\n> ").lower()

if q3 == "a":
    reward += 1
elif q3 == "b":
    fear += 1
elif q3 == "c":
    growth += 1

print("\nYour Motivation Type:")

if reward > fear and reward > growth:
    print("You are primarily reward-motivated.")
elif fear > reward and fear > growth:
    print("You are primarily fear-motivated.")
elif growth > reward and growth > fear:
    print("You are primarily growth-motivated.")
else:
    print("You have a mixed motivation style (Reward / Fear / Growth).")

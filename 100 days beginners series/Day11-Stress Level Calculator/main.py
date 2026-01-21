stress = 0

print("Answer with yes or no\n")

sleep = input("Did you sleep well last night? ").lower()
if sleep == "no":
    stress += 2

rush = input("Did you feel rushed or pressured today? ").lower()
if rush == "yes":
    stress += 2

breaks = input("Did you take short breaks today? ").lower()
if breaks == "no":
    stress += 1

exercise = input("Did you exercise or move your body today? ").lower()
if exercise == "no":
    stress += 1

overthink = input("Did you overthink or worry a lot today? ").lower()
if overthink == "yes":
    stress += 2

print("\nYour Stress Level:")

if stress <= 2:
    print("Low stress. You seem fairly relaxed today.")
elif 3 <= stress <= 5:
    print("Moderate stress. Take small breaks and breathe.")
else:
    print("High stress. Your body and mind may need rest and care.")

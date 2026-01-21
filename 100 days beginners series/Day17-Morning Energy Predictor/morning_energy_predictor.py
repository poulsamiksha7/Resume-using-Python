energy = 0

sleep = input("Did you sleep well last night? (yes/no): ").lower()
mood = input("How is your mood this morning? (good/okay/bad): ").lower()

if sleep == "yes":
    energy += 2
else:
    energy += 0

if mood == "good":
    energy += 2
elif mood == "okay":
    energy += 1
else:
    energy += 0

print("\nMorning Energy Level:")

if energy <= 1:
    print("Low energy. Take it slow this morning.")
elif 2 <= energy <= 3:
    print("Moderate energy. You can manage steady tasks.")
else:
    print("High energy! Great time to do important work.")

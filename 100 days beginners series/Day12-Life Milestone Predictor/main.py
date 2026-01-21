age = int(input("Enter your age: "))

if 13 <= age <= 18:
    print("This stage is often about discovering who you are and building confidence.")

elif 19 <= age <= 25:
    print("This stage is about learning, exploring careers, and finding your direction.")

elif 26 <= age <= 35:
    print("This stage often focuses on career growth, independence, and stability.")

elif 36 <= age <= 50:
    print("This stage is about long-term goals, growth, and creating balance in life.")

elif 51 <= age <= 65:
    print("This stage often brings reflection, health focus, and mentoring others.")

elif age >= 66:
    print("This stage is about wisdom, legacy, and enjoying life.")

else:
    print("Please enter a valid age (13 or above).")

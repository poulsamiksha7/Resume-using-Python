user_input=input("What dreams are you having ?").lower()

if  "fall" in user_input or "falling" in user_input:
    print("This dream may symbolize fear of losing control or insecurity in waking life")
elif "fly" in user_input or "flying" in user_input:
    print("This dream may reflects a desire for freedom, confidence, or  rising above limitations.")
elif "water" in user_input:
    print("Water in dreams often represnts emotions or emotional depth.")
elif "chase" in user_input or "chasing" in  user_input:
    print("Being chased may symbolize avoidance, stress, or unresolved issues.")
elif "teeth" in user_input:
    print("Dream about teeth can relate to insecurity, self-image, or fear of judgement.")
elif "exam" in user_input or "test" in user_input:
    print("Exam dreams often reflect pressure, self-evaluation, or fear of failure.")
elif "dark" in user_input or "darkness" in user_input:
    print("Darkness in dreams may symbolize uncertinaty or the unknown.")
elif "lost" in user_input:
    print("Feeling lost in a dream may reflect confusion or searching for direction.")
else:
    print("Some dreams don't have clear symbol and may simply reflect daily thoughts")
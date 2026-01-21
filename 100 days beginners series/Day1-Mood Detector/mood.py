from datetime import datetime
user_input=input("Enter Today's Mood...")
u_input=user_input.lower()
mood="Unknown"
if "happy" in u_input:
    print("Joy arrived without permission, and I let it stay.")
    mood="happy"
elif "sad" in u_input:
    print("Even heavy days are part of becoming whole.")
    mood="sad"
elif "anxious" in u_input:
    print("Anxity speaks loudly, but it doesn't decide the future.")
    mood="anxious"
elif "tired" in u_input:
    print("Some strength looks like slowing down.")
    mood="tired"
else:
    print("Not every feeling needs a name to be valid.")
now=datetime.now()
date=now.strftime("%d%m%Y")
time=now.strftime("%H%M")

with open("mood_journal.txt","a") as file:
    file.write(f"{date} | {time} | {user_input} | Mood: {mood} \n ")
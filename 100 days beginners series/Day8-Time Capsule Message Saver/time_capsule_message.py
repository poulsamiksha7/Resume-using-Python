from datetime import datetime
user_input=input("Enter your Message: ")

now=datetime.now()
date=now.strftime("%Y-%m-%d")
time=now.strftime("%H%M")

with open("message.txt","a") as file:
    file.write(f"{date} | {time}\n")
    file.write(f"{user_input}\n")
    file.write(f"-"*30+"\n")

print("Your message has been saved to the time capsule")


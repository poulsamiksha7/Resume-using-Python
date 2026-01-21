user_input=input("Enter your Name: ")
u_input=user_input.lower()
if len(u_input)<=4:
    print("confident,direct")
elif 5<= len(u_input)>=5:
    print("balanced,adaptable")
elif len(u_input)>=8:
    print("thoughtful,deep thinker")
else:
    print("Invalid Input !")
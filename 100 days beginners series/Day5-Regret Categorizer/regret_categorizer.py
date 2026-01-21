user_input=input("What is something you regret? ").lower()

if any(word in user_input for word in ["job",'work',"career","interview","company","money"]):
    print("This regret relates to your journey.")
elif any(word in user_input for word in["study","college","exam","degree","school","course"]):
    print("This regret is connected to your learning or education.")
elif any(word in user_input for word in ["friend","family","parents","love","relationship","breakup"]):
    print("This regret is belongs to your relationship.")
elif any(word in user_input for word in["health","sleep","diet","exercise","illness","stress"]):
    print("This regret is related to your health and well- belong.")
elif any(word in user_input for word in ["confidence","fear","time","discipline","consistency","myself"]):
    print("This regret reflects personal growth and self-reflection.")
else:
    print("This regret doesn't fit one category and that's okay.")
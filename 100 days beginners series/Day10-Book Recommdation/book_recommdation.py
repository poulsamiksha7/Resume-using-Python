user_input = input("How are you feeling today? ").lower()

if "happy" in user_input or "excited" in user_input:
    print("You might enjoy a feel-good fiction or comedy book.")

elif "sad" in user_input or "down" in user_input:
    print("A comforting book like poetry or inspirational fiction may help.")

elif "anxious" in user_input or "stressed" in user_input:
    print("Consider a calming self-help or mindfulness book.")

elif "tired" in user_input or "exhausted" in user_input:
    print("Short stories or light, easy reads could be perfect right now.")

elif "bored" in user_input:
    print("A mystery, thriller, or adventure book might keep you engaged.")

elif "motivated" in user_input or "focused" in user_input:
    print("You may enjoy non-fiction, biographies, or productivity books.")

elif "calm" in user_input or "peaceful" in user_input:
    print("Philosophy, nature writing, or slow fiction could suit your mood.")

else:
    print("A general fiction book is a gentle place to start, no matter the mood.")

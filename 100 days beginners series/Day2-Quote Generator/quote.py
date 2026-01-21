import random
happy_quotes=[
    "Happiness does'nt shout - it quietly settles in the moment you notice it.",
    "Some days don't need fixing - just feeling",
    "Joy arrived without permission, and I let it stay"
]
sad_quotes=[
    "Even heavy days are part of becoming whole",
    "Some feelings don't ask for solutions - only space",
    "It's okay to move slowly when your heart feels tired"
]
anxious_quotes=[
    "Breath, You are here , That is enough for now",
    "Anxiety speaks loudly, but it doesn't decide the future",
    "This moment is difficult , but it is not present"
]
tired_quotes=[
    "Rest is not quitting,it's listening",
    "Some strength looks like slowing down",
    "Even the strongest minds need pause"
]
neutral_quotes=[
    "Not every feeling needs a name to be valid",
    "Today didn't come with clarity, and that's okay."
]

user_input=input("Enter your mood...")
u_input=user_input.lower()
if "happy" in u_input:
    print(random.choice(happy_quotes))
elif "sad" in u_input:
    print(random.choice(sad_quotes))
elif "anxious" in u_input:
    print(random.choice(anxious_quotes))
elif "tired" in u_input:
    print(random.choice(tired_quotes))
else:
    print(random.choice(neutral_quotes))
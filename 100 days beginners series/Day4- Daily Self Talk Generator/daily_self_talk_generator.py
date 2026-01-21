import random
calm_affirmations = [
    "Breathe. This moment is safe.",
    "Slow down — nothing is required of you right now."
]

motivation_affirmations = [
    "You are capable of more than you think.",
    "Start small. Progress still counts."
]

confidence_affirmations = [
    "Your voice matters.",
    "You are allowed to take up space."
]

rest_affirmations = [
    "Rest is productive.",
    "You don’t have to earn your rest."
]

neutral_affirmations = [
    "You are doing your best, and that is enough.",
    "This day does not define you."
]

user_input = input("What do you need today? ").lower()

if any(word in user_input for word in ["calm", "peace", "stressed", "anxious", "overwhelmed"]):
    print(random.choice(calm_affirmations))

elif any(word in user_input for word in ["motivation", "focus", "lazy", "stuck"]):
    print(random.choice(motivation_affirmations))

elif any(word in user_input for word in ["confidence", "nervous", "scared", "doubt", "insecure"]):
    print(random.choice(confidence_affirmations))

elif any(word in user_input for word in ["rest", "tired", "exhausted", "sleepy", "burnout"]):
    print(random.choice(rest_affirmations))
else:
    print(random.choice(neutral_affirmations))
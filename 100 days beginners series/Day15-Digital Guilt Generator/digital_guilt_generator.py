import random

study_guilt = [
    "Your future self is judging you quietly.",
    "That chapter didn’t read itself, you know."
]

workout_guilt = [
    "Your dumbbells are feeling abandoned.",
    "That workout skipped you too."
]

sleep_guilt = [
    "Sleep was waiting… you ghosted it.",
    "Your pillow remembers."
]

work_guilt = [
    "Deadlines don’t forget. Ever.",
    "That task is still staring at you."
]

general_guilt = [
    "We’re not mad. Just disappointed.",
    "Tomorrow-you is already tired."
]

user_input = input("What task did you skip today? ").lower()

if any(word in user_input for word in ["study", "homework", "revise", "learn"]):
    print(random.choice(study_guilt))

elif any(word in user_input for word in ["workout", "gym", "exercise"]):
    print(random.choice(workout_guilt))

elif any(word in user_input for word in ["sleep", "bed", "rest"]):
    print(random.choice(sleep_guilt))

elif any(word in user_input for word in ["work", "deadline", "task"]):
    print(random.choice(work_guilt))

else:
    print(random.choice(general_guilt))

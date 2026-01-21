values_input = input("Enter your values (separate with commas): ")

values = [v.strip() for v in values_input.split(",")]

scores = {}

for value in values:
    score = int(input(f"How important is '{value}' (1-5)? "))
    scores[value] = score

ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)

print("\nYour Value Priority List:")
for i, (value, score) in enumerate(ranked, start=1):
    print(f"{i}. {value} (importance: {score})")

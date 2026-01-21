thoughts = input("Write your messy thoughts (separate with commas): ")

thought_list = thoughts.split(",")

clean_thoughts = []

for thought in thought_list:
    clean_thoughts.append(thought.strip())

print("\nYour Clean Thought List:")
for i, item in enumerate(clean_thoughts, start=1):
    print(f"{i}. {item}")

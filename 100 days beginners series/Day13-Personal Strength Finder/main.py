strengths=0
print("Answer with A or B\n")

resilience=input("When something goes wrong, you usually \n A)Try again \n B)Feel discouraged \n").lower()
if resilience == "A":
    strengths+=2
empthy=input("When a friend is upset, you \n A)Listen \n B)Avoid \n").lower()
if empthy=="A":
    strengths+=2
focus=input("When working you\n A)Stay Focused \n B)Get distracted \n").lower()
if focus=="A":
    strengths+=1
creativity=input("When solving a problem\n A)Try new ideas\n B)Follow rules\n").lower()
if creativity=="A":
    strengths+=1
leadership=input("In group tasks, you\n A)Take charge \n B)Wait \n").lower()
if leadership=="A":
    strengths+=2
discipline=input("With golas, you \n A)Stay Consistent \n B)Give up\n").lower()
if discipline=="A":
    strengths+=1

print("\nYour Strengths: ")

if strengths<=2:
    print("Developing Strength")
elif 3<=strengths<=5:
    print("Emerging Strength")
else:
    print("Strong Strength")
import random
colour=["red","blue","yellow","purple","green"]
print(colour,"These are your choices of colour ")
computer=[]
x=4
y=4
colour1=[]
while x>=1:
    computer1=random.choice(["red","blue","yellow","purple","green"])
    computer.append(computer1)
    x=x-1

while y>=1:
    quest=input("Enter a colour from your choices.")
    colour1.append(quest)
    y=y-1

z=0
right=0
wrong=0
while z!=4:
    for X in colour1:
        if X in computer:
            place=colour1.index(X)
            place2=computer.index(X)
            if place==place2:
                right=right+1
                z=z+1
            else:
                wrong=wrong+1
                z=z+1

if right==4:
    print("You got it right")
else:
    colour1.clear
    y=4
    while y>=1:
        quest=input("Enter a colour from your choices.")
        colour1.append(quest)
        y=y-1
    
                
    
    
    

    



print(computer)
print(colour1)


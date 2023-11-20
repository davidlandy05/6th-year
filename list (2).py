"""
1.
Sport=["Football","baseball"]
user=input("Enter your favorite sport")
Sport.append(user)
print(Sport)
"""
"""
2.
Subjects=["Maths","English," "pe","Messi","pessi","blessi"]
Nope=input("What is your least favorite subject")
Subjects.remove(Nope)
print(Subjects)

3.
Colour=["Red","Blue","Yellow","Green","Purpe","Violet","Black","Orange","grey","white"]
Number1=Colour[0:4]
Number2=Colour[5:9]
print(Number1)
print(Number2)

4.
Number=[111,222,333,444]
print(Number)
user=input("Enter a number and if its in the list it will be removed")
user=int(user)
if user in Number:
    Number.remove(user)
print(Number)

5.
Party=[]
user0=input("Who is the person you want to invite to your party?")
user1=input("Who is the person you want to invite to your party?")
user2=input("Who is the person you want to invite to your party?")
Party.append(user0)
Party.append(user1)
Party.append(user2)
print(Party)

user3=input("Do you wish to invite more people")
user3=user3.lower()
while user3=="yes":
    user=input("Who is the person you want to invite to your party?")
    Party.append(user)
    user3=input("Do you still want to add people")
"""
6.
Party=[]
user0=input("Who is the person you want to invite to your party?")
user1=input("Who is the person you want to invite to your party?")
user2=input("Who is the person you want to invite to your party?")
Party.append(user0)
Party.append(user1)
Party.append(user2)
print(Party)

user3=input("Do you wish to invite more people")
user3=user3.lower()
while user3=="yes":
    user=input("Who is the person you want to invite to your party?")
    Party.append(user)
    user3=input("Do you still want to add people")
Bye=input("Enter a name one of your party member")
Mush=Party.index(Bye)
print(Mush)
Ask=input("Do you still want that person to come")
Ask=Ask.lower
if Ask=="no":
    if
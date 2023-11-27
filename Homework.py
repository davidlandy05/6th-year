X=0
while X>0:
    f_name=input("What is your first name")
l_name=input("What is your last name")
age=input("What is your age")
eircode=input("What is your eircode")
age=int(age)
vaccine=""
Terminate=""

if age>=50:
    vaccine="Adeno"
if age<=49:
    if age>=12:
         vaccine="MRDR"

age=str(age)

last=eircode[-1]
last=int(last)

if last/2==0:
    eircode="Northfield"
else:
    eircode="Eastwood"

print("Your name is "+ f_name + l_name +" and you are "+ age +" years old")
print("You are getting "+vaccine)
print("You must attend "+eircode+" to get your vaccine")
k=input("If you are done please enter END")
if q="end":
    break



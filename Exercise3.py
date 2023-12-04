name=input("What is your name")
def username(name):
    fortnite = "hello "+name+ " Welcome to the percentage calculator"
    return fortnite
name=username(name)
print(name)
student_name = input("Please enter the students name: ")
student_score = float(input("Please enter the students mark: "))
examtotal=int(input("How many marks is the test worth?"))
score_as_a_percentage=(student_score/examtotal)*100
score_as_a_percentage=round(score_as_a_percentage,1)
score=""
if score_as_a_percentage>0:
    if score_as_a_percentage<59:
        score="C"
elif score_as_a_percentage>60:
    if score_as_a_percentage<79:
        score="B"\
elif score_as_a_percentage>80:
    score="A"
else:
    print("Invalid score")
    
print("This test was out of", examtotal ,"marks")
print(student_name,"scored",score_as_a_percentage,"%. They got a",score)
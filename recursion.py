numbers=[1,2,3,4,5,6,7,8,9,10,]
amount=len(numbers)
total=0


def total(numbers):
    if len(numbers)==0:
        return 0
    else:
        return numbers[0]+ total(numbers[1:])
print(total(numbers))

ask=int(input("Enter a number"))
total1=0
def fact(ask):
    if ask==0:
        return 1
    else:
        return ask*fact((ask-1))
print(fact(ask))

ask1=input("Enter a number")
def add(ask1):
    if int(ask1)<10:
        return int(ask1)                                   
    else:
        return int(ask1[0])+add(ask1[1:])
print(add(ask1)) 
        
runningTotal=0
number1=12
runningTotal=runningTotal+number1
number2=24
runningTotal=runningTotal+number2
number3=36
runningTotal=runningTotal+number3
number4=48
runningTotal=runningTotal+number4
print(runningTotal)

fin=open("daffodils.txt")
print(fin)
for line in fin:
    print(line.strip())
fin.close()

runningTotal1=0
fin=open("daffodils.txt")
print(fin)
for line in fin:
    print(line.strip())
    runningTotal1 =runningTotal1+1
fin.close()
print(runningTotal1)

runningTotal2=0
Sum=0
fin=open("cal1.py")
print(fin)
for line in fin:
    print(line.strip())
    runningTotal2=runningTotal2=1
    if(line.isdigit()):
        print(line)
fin.close()







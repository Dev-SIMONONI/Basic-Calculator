'''
isMarried=True
isMarried=False
print(isMarried)


football="i love it "
print(bool(football))

cricket="am not a fan"
print(bool(cricket))

cooking=""
print(bool(cooking))

jogging=None
print(bool(jogging))



num1=-1
print(bool(num1))

num2=0.5
print(bool(num2))

num3=0
print(bool(num3))

num4=0.0
print(bool(num4))



#LOGICAL
Fnum=5
Snum=0
print(Fnum and Snum)
if Fnum or Snum:
     print("valid")
'''
#Arimethic operator
#Plus + means overloaded means to can be use for diff operation
print(""" ******************************
Welcome to a simple caculator app \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division
***********************""")

print("Enter two number to add")
firstNum=input("first number >>>  ")
secNum=input("second number >>>  ")
sum=float(firstNum) + float(secNum)
print(f"{firstNum} + {secNum} = {sum}")

print(""" ********************************
""")

print("#Substraction")
print("Enter two number to substract")
firstNum=input("first number >>>  ")
secNum=input("second number >>>  ")
sum=float(firstNum) - float(secNum)
print(f"{firstNum} - {secNum} = {sum}")

print("""***************************
""")

print("#Multiplation")
print("Enter two number to multiply")
firstNum=input("first number >>>  ")
secNum=input("second number >>>  ")
sum=float(firstNum) * float(secNum)
print(f"{firstNum} * {secNum} = {sum}")

print("""**************************
""")

print("#Division")
print("Enter two number to divid")
firstNum=input("first number >>>  ")
secNum=input("second number >>>  ")
sum=float(firstNum) / float(secNum)
print(f"{firstNum} / {secNum} = {sum}")

print("""************************
""")

print("#Exponential")
print("Enter two number to exponential")
firstNum=input("first number >>>  ")
secNum=input("second number >>>  ")
sum=float(firstNum) ** float(secNum)
print(f"{firstNum} ** {secNum} = {sum}")

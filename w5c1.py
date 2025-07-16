#Arimethic operator
#Plus + means overloaded means to can be use for diff operation
print(""" ******************************
Welcome to a simple caculator app \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Floor
***********************""")

print("Enter two number to add")
firstNum=input("first number >>>  ")
secNum=input("second number >>>  ")
sum=float(firstNum) + float(secNum)
print(f"{firstNum} + {secNum} = {sum:.2f}")

print(""" ********************************
""")

print("#Substraction")
print("Enter two number to substract")
firstNum=input("first number >>>  ")
secNum=input("second number >>>  ")
subtract=float(firstNum) - float(secNum)
print(f"{firstNum} - {secNum} = {subtract:.2f}")

print("""***************************
""")

print("#Multiplation")
print("Enter two number to multiply")
firstNum=input("first number >>>  ")
secNum=input("second number >>>  ")
multiply=float(firstNum) * float(secNum)
print(f"{firstNum} * {secNum} = {multiply:.2f}")

print("""**************************
""")

print("#Division")
print("Enter two number to divid")
firstNum=input("first number >>>  ")
secNum=input("second number >>>  ")
div=float(firstNum) / float(secNum)
print(f"{firstNum} / {secNum} = {div:.2f}")

print("""************************
""")

print("#Exponential")
print("Enter two number to exponential")
firstNum=input("first number >>>  ")
secNum=input("second number >>>  ")
exp=float(firstNum) ** float(secNum)
print(f"{firstNum} ** {secNum} = {exp:.2f}")

print("""************************
 """)
 
print("#Floor")
print("Enter two number to Floor")
firstNum=input("first number >>>  ")
secNum=input("second number >>>  ")
floor=float(firstNum) // float(secNum)
print(f"{firstNum} // {secNum} = {floor:.2f}")


print("------------------")
print("+ for addition")
print("- for subtraction")
print("/ for division [float division]")
print("// for division [integer division]")
print("* for multiplication")
print("------------------")

operand = str(input("Enter your operand : "))
num1 = int(input("Enter num1 : "))
num2 = int(input("Enter num2 : "))

print("Answer : ", end=" ")

if(operand == '+'):
    print(num1 + num2)
elif(operand == '-'):
    print(num1 - num2)
elif(operand == '/'):
    print(num1 / num2)
elif(operand == '//'):
    print(num1 // num2)
elif(operand == '*'):
    print(num1 * num2)
num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))
op = input("enter the operator( + , - , * , /)")
if op == "+":
    print("answer is ", num1 + num2)
elif op == "-":
    print("answer is " , num1 - num2)
elif op == "*":
    print("anwer is " , num1 * num2)
elif op == "/":
    if num2 != 0:
        print("answer is " , num1 / num2)
    else:
        print("error!: division by zero")
else:
    print("invalid operator")

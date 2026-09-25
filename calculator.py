# آلة حاسبة بسيطة
num1 = float(input("الرقم الأول: "))
op = input("العملية (+, -, *, /): ")
num2 = float(input("الرقم التاني: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("عملية مش صح")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

choice = int(input("Enter Choice 1. Add 2. Substract 3. Multiply 4. Divide 5. Power"))

if choice == 1:
    print(num1, "+", num2, "=", num1+num2)

elif choice == 2:
    print(num1, "-", num2, "=", num1-num2)

elif choice == 3:
    print(num1, "*", num2, "=", num1*num2)

elif choice == 4:
    print(num1, "/", num2, "=", num1/num2)
elif choice == 5:
    print(num1, "^", num2, "=", num1**num2)
else:
    print("Invalid input")
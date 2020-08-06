'''
Exercise-2
The Faulty Calculator
Write a program of calculator which will
correctly solve all arguments except
45*3=555, 56+9=77, 56/6=4  these

You should take a input operator including two numbers.
'''

while(1):
    num1 = float(input("Enter First Num:"))
    num2 = float(input("Enter Second Num:"))
    operator = input("Choose a operator : +,*,/ ")

    if num1 == 56 and num2 == 9 and operator == "+":
        print("Sum=77.00")
    elif num1 == 45 and num2 == 3 and operator == "*":
        print("Multi=555.00")
    elif num1 == 56 and num2 == 6 and operator == "/":
        print("Div=4.00")
    elif operator == "+":
        sum = num1 + num2
        print("Sum=", sum)
    elif operator == "*":
        multi = num1 * num2
        print("Multi=", multi)
    elif operator == "/":
        div = num1 / num2
        print("Div=", div)
    else:
        print("Error !! Cheak The Input")


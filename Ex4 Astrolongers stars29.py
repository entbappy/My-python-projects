# Exercise 4 (Pattern printing)

con1 = True
con2 = False
while(1):
    num = int(input("Enter the num="))
    value = int(input("Enter the value (0 or 1)="))
    if value == con1:
        for i in range(1,num+1):
            print(i*"*")

    elif value == con2:
        for v in range(num,0,-1):
            print(v*"*")

    else:
        print("Not valid!!")










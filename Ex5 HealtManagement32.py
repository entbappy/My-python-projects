import datetime
def getdate():
    return datetime.datetime.now()

def keep(k):
    if k == 1:
        a = int(input("Enter 1 for Exercise and 2 for Food="))
        if (a == 1):
            val = input("Type here..\n")
            with open("BappyEx.txt","a") as add:
                add.write(str([str(getdate())]) + ":" + val + "\n")
            print("Successfully Written...")
        elif (a == 2):
            val = input("Type here..\n")
            with open("BappyFood.txt","a") as add:
                add.write(str([str(getdate())]) + ":" + val + "\n")
            print("Successfully Written...")
    elif k == 2:
        a = int(input("Enter 1 for Exercise and 2 for Food="))
        if (a == 1):
            val = input("Type here..\n")
            with open("HarryEx.txt", "a") as add:
                add.write(str([str(getdate())]) + ":" + val + "\n")
            print("Successfully Written...")
        elif (a == 2):
            val = input("Type here..\n")
            with open("HarryFood.txt", "a") as add:
                add.write(str([str(getdate())]) + ":" + val + "\n")
            print("Successfully Written...")
    elif k == 3:
        a = int(input("Enter 1 for Exercise and 2 for Food="))
        if (a == 1):
            val = input("Type here..\n")
            with open("HermioneEx.txt", "a") as add:
                add.write(str([str(getdate())]) + ":" + val + "\n")
            print("Successfully Written...")
        elif (a == 2):
            val = input("Type here..\n")
            with open("HermioneFood.txt", "a") as add:
                add.write(str([str(getdate())]) + ":" + val+ "\n")
            print("Successfully Written...")
    else:
        print("Not valid!! Please choose the correct one 1.Bappy 2.Harry 3.Hermione")

def retrieve(k):
    if k == 1:
        a =  int(input("Enter 1 for Exercise and 2 for Food="))
        if (a == 1):
            with open("BappyEx.txt") as add:
                for i in add:
                    print(i, end=" ")
        elif (a == 2):
            with open("BappyFood.txt") as add:
                for i in add:
                    print(i, end=" ")
    elif k == 2:
        a = int(input("Enter 1 for Exercise and 2 for Food="))
        if (a == 1):
            with open("HarryEx.txt") as add:
                for i in add:
                    print(i, end=" ")
        elif (a == 2):
            with open("HarryFood.txt") as add:
                for i in add:
                    print(i, end=" ")
    elif k == 3:
        a = int(input("Enter 1 for Exercise and 2 for Food="))
        if (a == 1):
            with open("HermioneEx.txt") as add:
                for i in add:
                    print(i, end=" ")
        elif (a == 2):
            with open("HermioneFood.txt") as add:
                for i in add:
                    print(i, end=" ")
    else:
        print("Not valid!! Please choose the correct one 1.Bappy 2.Harry 3.Hermione")


print("      Health Management System")

num = int(input("Enter 1 for Log and 2 for Retrieve ="))
if num == 1:
    name = int(input("Enter name 1.Bappy 2.Harry 3.Hermione="))
    keep(name)
else:
    name = int(input("Enter name 1.Bappy 2.Harry 3.Hermione="))
    retrieve(name)









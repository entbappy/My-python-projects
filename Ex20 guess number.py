n = [1,2,3,4,5,6,7,8]
i = 0
guess = 0
while(i<4):
    num = int(input("Enter Your guess number="))
    i= i+1
    guess=guess+1
    for s in n:
        if num==6:
            print("You Won....Your guess was:",guess)
            break
        elif num>8:
            print("Out of number")
            break

        elif num==7:
            print("You are nearly overcome")
            break
        elif num==4:
            print("You are  near")
            break
        else:
            print("No")
            break

else:
    print("You Losser")



# i = 0
# guess = 0
# while(i<4):
#     num = int(input("Enter Your guess number="))
#     i= i+1
#     guess=guess+1
#
#     if num==6:
#         print("You Won....Your guess was:",guess)
#
#     elif num==5:
#         print("You are very near")
#
#
#     elif num==7:
#         print("You are nearly overcome")
#
#     elif num==4:
#         print("You are  near")
#
#     else:
#          print("No")
#
#
# else:
#     print("You Losser")
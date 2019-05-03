import random
random = random.randrange(1,1001)
print(random)
for i in range(3):
    if i == 0:
        print("First chance")
    elif i == 1:
        print("Second chance")
    elif i == 2:
        print("Third chance")
        
    try:
        num = int(input("Enter some number in between 1 to 1000:-"))
        if num>random:
            diff = num-random
            if diff>100:
                print("Entered number is too bigger than random number")
            else:
                print("Entered number is closed to random number")
        elif num<random:
            diff = random-num
            if diff>100:
                print("Entered number is too less than random number")
            else:
                print("Entered number is closed to random number")
        elif num == random:
            print("correct guess")
            print("You won the game!")
            break
    except:
        print("Wrong input! please enter number only")
print("ALL CHANCES ARE OVER")
print("EXIT")

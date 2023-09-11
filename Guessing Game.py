import random
start = int(input("Enter Lower bound:- "))
end = int(input("Enter Upper bound:- "))
randomNumber = random.randrange(start,end)
stop = False
i=1
while stop==False:
    n = int(input("Guess a number:- "))
    if n==randomNumber:
        if i==1:
            print("Congratulations you did it in",str(i)+"st try")
        elif i==2:
            print("Congratulations you did it in",str(i)+"nd try")
        elif i==3:
            print("Congratulations you did it in",str(i)+"rd try")
        elif i>3 and i<=7:
            print("Congratulations you did it in",str(i)+"th try")
        stop = True
    elif n<randomNumber:
        print("You guessed too small!")
    else:
        print("You guessed too high!")
    i+=1
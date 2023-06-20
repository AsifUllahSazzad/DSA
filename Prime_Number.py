start,end = map(int,input("Enter start and end numbers: ").split())

if start>1:
    for i in range(start,end+1):
        for j in range(start,i):
            if i%j==0:
                break
        else:
            print(i,end=" ")
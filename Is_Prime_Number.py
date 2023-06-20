n = int(input())
stop = True
for i in range(2,n):
    if n%i==0:
        stop = False
        break
if stop==True:
    print(n," is a prime number.")
else:
    print(n," is a composite number.")
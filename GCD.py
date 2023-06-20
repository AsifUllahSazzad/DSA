a,b = map(int,input("Enter two numbers: ").split())
gcd = 0
i=1
while a>i and b>i:
    if a%i==0 and b%i==0:
        gcd = i
    i+=1
print("The gcd of",a,"and",b,"is:",gcd)
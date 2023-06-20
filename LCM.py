a,b = map(int,input("Enter two numbers: ").split())
gcd =0
lcm=1
i=1
while a>i and b>i:
    if a%i==0 and b%i==0:
        gcd = i
        lcm = a*b//gcd
    i+=1
print("The lcm of",a,"and",b,"is:",lcm)
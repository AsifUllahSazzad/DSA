n = int(input("Input an octal number: "))
i = 0
ans = 0
temp = n

while temp!=0:
    num = temp%10
    ans = ans+num*8**i
    temp = temp//10
    i+=1

print("The Octal Number:",n)
print("The equivalent Decimal Number:",ans)
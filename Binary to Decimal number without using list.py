n = int(input("Input a binary number: "))

pw = 1
Decimal = 0
temp = n

while temp!=0:
    num = temp%10
    if num==1:
        Decimal+=pw
    pw*=2
    temp//=10

print("The Binary Number:",n)
print("The equivalent Decimal Number:",Decimal)
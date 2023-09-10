n = int(input("Input a decimal number: "))
result =''

while n!=0:
    if n%2==0 or n%2==1:
        ans = n%2
        result = str(ans)+result
        n = n//2
print("Binary number equivalent to said decimal number is:",result)
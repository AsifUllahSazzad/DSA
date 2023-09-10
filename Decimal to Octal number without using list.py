n = int(input("Enter a number to convert: "))
result = ""
temp = n

while temp!=0:
    num = temp%8
    result = str(num)+result
    temp = temp//8

print("The Octal of",n,"is:",result)
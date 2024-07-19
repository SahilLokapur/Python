r=n=int(input("Enter a number:"))
count=0
digits = [int(digit) for digit in str(n)]
print(digits)
while n!=0:
    n=n//10
    count=count + 1
t=count
val=digits[0]**t + digits[1]**t + digits[2]**t
if val==r:
    print(r,"is an armstrong number")
    print(r,"=",digits[0],"^",t,"+", digits[1],"^",t,"+", digits[2],"^",t,"=",val)
else:
    print(r,"is not an armstrong number")
    print(r,"=",digits[0],"^",t,"+", digits[1],"^",t,"+", digits[2],"^",t,"=",val)


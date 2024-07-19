n=int(input("Enter a number:"))

def prime(n):
    count = 0
    for i in range(2, n + 1):
        if n % i == 0:
            count = count + 1
    if count == 1:
     print("Given number is prime")
    else:
     print("Given number is not prime")
prime(n)
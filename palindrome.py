def isPalindrome():
    string=input("Enter a string :")
    left_pos = 0
    right_pos = len(string) - 1
    if right_pos == left_pos:
        return f"Invalid String"
    else:
        while right_pos >= left_pos:
            if not string[left_pos] == string[right_pos]:
                return "Entered string is not a palindrome"
            left_pos += 1
            right_pos -= 1
        return "Entered string is a palindrome"
print("1.Perform")
print("2.Exit")
ch=int(input("Enter your choice:"))
while ch != 2:
    print(isPalindrome())
    ch=int(input("Choice"))


#Code for Plaindrome check.
n = int(input("Enter number: "))
temp = n
rev = 0

for i in range(len(str(n))):
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10

if temp == rev:
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
    

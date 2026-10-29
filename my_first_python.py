#to find the palindrome of a number
n1=int(input("Enter a number:"))
n2=n1
rev=0
while n2>0:
    r=n2%10
    rev=rev*10 + r
    n2//=10
if rev==n1:
    print("Palindrome")
else:
    print("Not palindrome")
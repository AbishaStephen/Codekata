s=int(input("Enter the value for a"))
a=int(input("Enter the value for b"))
n=s+a
sa=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(sa==rev):
    print("The sum of a and b is a palindrome!")
else:
    print("The sum of a and b is not a palindrome!")

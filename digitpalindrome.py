n=int(input("Enter number:"))
palin=n
rev=0
while(n>0):
    digit=n%10
    rev=rev*10+digit
    n=n//10
if(palin==rev):
    print(str(palin)+ " number is a palindrome")
else:
    print(str(palin)+" number is not a palindrome")                                                   

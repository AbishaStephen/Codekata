sum=0
    flag=0
    n=input("Enter the number")
    val=n
    while n>0:
        q=n/10
        r=n%10
        n=q

        sum=sum+(r*r*r)
    if(sum==val):
        print("Given number is  an  armstrong number")
    else:
         print("Given number is not an armstrong number")

n=input("Enter the number")
    n1=input("Enter the seed number")
    sum=1
    val=n
    while n>0:
        q=n/10
        r=n%10
        n=q
        sum=r*sum
        sum=n*sum
    if(sum==vals):
        print("It is  an  seed number")
    else:
         print("It is not an seed number")

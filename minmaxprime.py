min = int(input("Enter the minimum number: "))
max = int(input("Enter the maximum number: "))
min = 100
max = 1000
print("Prime numbers between",min,"and",max,"are:")
for num in range(min,max + 1):
     if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)

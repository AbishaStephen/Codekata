a = int(input("Enter a number: "))
fact = 1
if a < 0:
   print("Invalid Input")
elif a == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,a + 1):
       fact = fact*i
   print(str(fact)+ " is a factorial of" +str(a))

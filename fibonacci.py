def fib(n):
  if n<=1:
     return n
  else:
     return(fib(n-1)+fib(n-2))
num=int(input("Enter the number of terms"))
if num<=0:
   print("Please enter the positive number")
else:
   print("Fibonacci series:")
   for i in range(num):
          print(fib(i))

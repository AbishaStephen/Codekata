low = 100
 high = 2000
 low = int(input("Enter lower range: "))
 high = int(input("Enter upper range: "))
 for num in range(low, high + 1):
   order = len(str(num))
   sum = 0
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)

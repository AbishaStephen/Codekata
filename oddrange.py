low = 100
high = 1000


low = int(input("Enter lower range: "))
high = int(input("Enter upper range: "))
for i in range(low,high + 1):
 if (i%2)!= 0:
  print(i)

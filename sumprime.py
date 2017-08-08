limit = 100
lower=10
upper=100
def is_prime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True
print("Prime numbers between",lower,"and",upper,"are:")

for num in range(lower,upper + 1):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
sum = 0
count = 0
num = 2
while count != limit:
    if is_prime(num):
        sum += num
        count += 1
    num += 1

print sum

def red(num,k):
  if (k<=0):
    return num
  if (num==0):
    return 10
  l=red(num/10,k)*10+num%10
  m=red(num/10,k-1)
  if (l<m):
    return l
  else:
    return m
num=input("Enter the number")
k=input("Enter the number of digits")
print red(num,k)

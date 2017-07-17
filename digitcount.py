num=input("Enter the charaters")
digit=0
l=len(num)
#char=0
for i in range(l):
  if num[i].isdigit():
     digit +=1
print digit

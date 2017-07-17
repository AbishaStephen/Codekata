i=input("Enter the first number: ")
j=input("Enter the second number: ")
k=input("Enter the third number: ")
if(i>=j) and (i>=k):
  result=i
elif (j>=i) and (j>=k):
  result=j
else:
  result=k
print('The largest between three number is: ',result)

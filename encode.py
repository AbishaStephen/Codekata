s= input("Enter the first string:");
a= input("Enter the second string:");
l= len(s);
m=len(a);
res=""
result=""
for i in range(0,l):
  char=ord(s[i])+10
  if(char>122):
    a=char-122
    ch=97+a-1
  res+=chr(char)
result=a[0]
for i in range(1,m-1):
  ch1=ord(a[i])+10
  if(ch1>122):
    a1=ch1-122
    ch1=97+a1-1
  result+=chr(ch1)
result+=a[m-1]
print res
print result

s=input("Enter a string:")
st=s
alphabet="abcdefghijklmnopqrstuvwxyz"
s=s.lower()
rew=""
count=0
for char in s:
    for l in alphabet:
        if char==l and char not in rew:
            rew+=char
for char in alphabet:
    for l in rew:
        if l==char:
            count+=1
if(count==26):
    print(st+" is a pangram")
else:
    print(st+" is not a pangram")

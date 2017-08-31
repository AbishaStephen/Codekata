string = input("Enter the string")
string_shortener = ""
a = 0
s = 3
p_temp=0
s_temp=0
long = ""
for i in range(len(string)-2):
    string_shortener = string[a:s]
    if(string_shortener==string_shortener[::-1]):
       p_temp = a
       s_temp = s
       for u in range(1000):
           p_temp-=1
           s_temp +=1
           string_shortener = string[p_temp:s_temp]
           if(string_shortener == string_shortener[::-1]):
                if len(string_shortener)>len(long):
                    long = string_shortener
           else:
                break
    a+=1
    s+=1
print(long)

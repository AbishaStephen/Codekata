s=input("Enter the string")
    ch=['a','e','i','o','u','A','E','I','O','U']
    vow=[]
    cons=[]
    for i in s:
            if i in ch:
             vow.append(i)
            else:
                cons.append(i)
    print("The entered String is " +s)
    print(vow)
    print(cons)

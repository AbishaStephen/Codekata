s=input("Enter the string")
    flag=0
    for i in s:
     if i.isdigit()==False:
       print("Entered string is not a digit")
       flag=1
       break
     if(flag<>1):
      print("Is a digit")
      break

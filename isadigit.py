s=input("Enter the string")
    flag=0
    for i in s:
     if i.isdigit()==False:
       print("False")
       flag=1
       break
     if(flag<>1):
      print("True")
      break

year = int(input("Enter a year: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print(str(year)+ "  is a leap year".format(year))
       else:
           print(str(year)+ "  is not a leap year".format(year))
   else:
       print(str(year)+ "  is a leap year".format(year))
else:
   print(str(year)+ "  is not a leap year".format(year))

#user input
year=int(input("enter the year: "))
#condition for leap year
if (year%400==0) or(year%4==0 and year%100!=0):
    print (f"{year}is a leap year")
else:
    print(f"{year}is not a leap year")
    print("this code is written and executed by srishti erp 0231bca044")
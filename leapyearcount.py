
year=int(input("enter the year: "))
count= 0
for i in range (1, year):
    if(i%4==0 and i%100!=0) or(i%400==0):
        print (i,"is leap year")
        count+=1
    else:
        print(i,"is not leap year")

print("no of leap year is:",count) 
print("this program is run and executed by srishti erp 0231bca044")
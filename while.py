#wap to demonstrate continue statement
print("Q33.wap to demonstrate continue statement")
for num in range (10):
    if num%2==0:#to check if a number is even
        continue #skip the rest of the loop body for even numbers
    print (num) #print only odd numbers
    
  #wap to demonstrate continue statement eith ehile loop  
print ("______________________________________________________________________________")
print("Q34.wap to demonstrate continue statement eith ehile loop")
count=0
while count<10:
    count+=1
    if count %2==0:#check if a number is even
        continue #skip the rest of the loop body for even numbers
    print (count)
print (" this program is written and executed by srishti(0231BCA044")

#wap to demonstrate break statement with for loop
print ("______________________________________________________________________________")
print("Q35.wap to demonstrate break statement with for loop")
for num in range (10):
    if num==5:#checks if number is 5
        break#exit the loop when numkber is 5
    print (num)
    
    #print number less than 5#"wap to demopnstrate break statement with while loop "
print ("______________________________________________________________________________")
print("Q36.wap to demopnstrate break statement with while loop ")
Count=0
while Count<10:
    Count+=1
    if Count %2==0:#check if a number is even
        break
    print (Count)
print (" this program is written and executed by srishti(0231BCA044")
    #wap to demonstrate try and except
print ("______________________________________________________________________________")
print("Q37.wap to demonstrate try and except")#exception handling
try:
    num= int (input ("enter a number:"))#set input as 0
    result=10/num
except ZeroDivisionError:
    print("error:Cannot divide by zero")
except ValueError:
    print("Error:Invalid input.please enter a valid input")
    print (" this program is written and executed by srishti(0231BCA044")

#wap to demonstrate try,except and else
print ("______________________________________________________________________________")
print("Q38.wap to demonstrate try,except and else")

try:
    num= int (input ("enter a number:"))#set input as 0
    result=10/num
except ZeroDivisionError:
    print("error:Cannot divide by zero")
except ValueError:
    print("Error:Invalid input.please enter a valid input")
else:
    print(f"the result is {result}.")
    print (" this program is written and executed by srishti(0231BCA044")
#wap to demonstrate try,except and finally
print ("______________________________________________________________________________")
print("Q39.wap to demonstrate try,except  and finally")
try:
    file= open ('example.txt ','r')
    content=file.read()
    print (content)
except FileNotFoundError:
    print ("error: the file was not found ")
finally:
    file.close()#ensures the file is closed whether or  not an exception occured 
    print (" this program is written and executed by srishti(0231BCA044")
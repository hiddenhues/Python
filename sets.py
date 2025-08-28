#wap to demonstrate set operations
from _typeshed import Self


print("wap to demonstrate set operations")
set1={1,2,3}
set2={3,4,5}
union =set1 | set2
intersection= set1&set2
difference=set1-set2
print("union:",union)
print("intersection:",intersection)
print("difference:",difference)
print (" this program is written and executed by srishti 0231BCA044")
print ("______________________________________________________________________________")
#wap to create &modify a dictonary
mydict={"name":"tanjiro","age":15}
mydict['age']=16
mydict['city']='tokyo'
print(mydict)
print ("______________________________________________________________________________")
#wap to access and nremove dictionary elements
my_dict={"name":"muichiro","age":14,"job":"hashira"}
name=my_dict.get('name')
print(my_dict)
my_dict.pop('job')
print(name)
print(my_dict)
print ("______________________________________________________________________________")

#wap to iterate through dictionary item
__dict__= {'a':1,'b':3,'c':4}
for key,value in __dict__.items():
    print(f"{key}:{value}")
print ("______________________________________________________________________________")
#wap to use built in itertors
MyLis=[1,2,3,4]
it=iter(MyLis)
for item in it:
        print(item)
print ("______________________________________________________________________________")
#wap to use iterator in a loop
print("#wap to use iterator in a loop")
ML=[1,2,3,4]
t=iter(ML)
for Item in t:
      print (Item)
print("________________________________________________________________________")
#wap to create and use custom iterator
class Reverse:
    def _init_ (self,data):
        self.data=data
        self.index=len(data)
    def _iter_ (self):
         return self
    def _next_ (self):
         if self.index==0:
            raise StopIteration
         self.index-=1
         return self.data[self.index]
    #create object
    rev= Reverse('giraffe')
    for char in rev:
         print(char)
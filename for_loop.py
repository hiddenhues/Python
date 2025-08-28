fruits=["apple","bannana","cherry"]
for i in fruits:
    print(i)

ages={"alice":30,"bob":25,"charlie":35}
for name,age in ages.items():
    print(f"{name} is {age} years old")

for i in range(3):
    print(i)
else:
    print("loop finished")

#nested looping:-
for i in range(2):
    for j in range(3):
        print(f"i={i},j={j}")

squares=[x**2 for x in range (5)]
print(squares)

fruits=["apple","banana","cherry"]
for index,fruits in enumerate(fruits):
    print(f"index{index}:{fruits}")
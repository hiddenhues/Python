
#Iterating through a byte objects

b=bytes([65,77,88,90])
print (b)
#accesing elements in abytes
print(b[0])
print(b[1])
#iterating through a bytes object
for byte in b:
    print(byte)
    print("\n")
    #ByteArray eg
    print ("Bytearray ")
    #creating bytearray object
ba = bytearray([10,11,12]) 

print (ba)
    #modifying elementd in bytearray
ba[0]=91
print(ba)
    #modifying element s to a bytearray
ba.append(30)
print (ba)

    #converting bytearray to bytes
b_converted= bytes(ba)
print(b_converted)
print("\n")
    #memoryveiw Example
print("memoryveiw Example")
    #creatinfg bytes obkject 
b_mv=bytes([65,66,67,68])
    #creating a memoryveiw object
mv= memoryview(b_mv)
print (mv[0])
    #slicing memoryveiw
mv_slice=mv[1:4]
print(mv_slice.tobytes())
    #creating a bytearray and a memoryview
ba_mv= bytearray([44,55,6,67])
mv_ba=memoryview(ba_mv)
    #Modyfying the orignal bytearray through memoryview
mv_ba[0]=97
print(ba_mv)
print("name:\n srishti \n erpid: \n 0231bca044")
bytetemp="A"
print(bytetemp)
print(bytes(bytetemp)) 
#need to photo compressing
#byte immutable
#bytearray mutable
#range 0 t0 256
list = [1,2,3,4,56,78,121,76,255]
b = bytes(list)
print(type(b))

#bytearray
list = [2,3,4,5,76,121,30,255]
b1 = bytearray(list)
b1[1] = 100
print(type(b1))
print(b1[1])
#end binary type data

#nonetype
x = None
print(type(x))


#sequence type
'''list,tuple,range'''
#list type(mutable)
li = ["ami" , "tui" ,"amr"]
print(li)
print(type(li))

#tuple type (immutable)
tu = ("ami" , "tmi")
print(tu)
print(type(tu))


#range type
ran = range(6)
print(ran)
for i in ran:
    print(i)
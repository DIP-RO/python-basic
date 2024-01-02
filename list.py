#change list item/access list item
hablu = ["change" , "website" , "Group" , "page"]
print(hablu[1])
hablu[1] = "dip"
print(hablu)

#added item
list  = ["dip","anim","toma", "tanu" , "shuvra"]
list.append("ariyan")
print(list)

list.insert(1,"ap")
print(list)

#remove list item
this = ["dip","anim","toma", "tanu" , "shuvra"]
this.remove("dip")
print(this)
this.pop(1)
print(this)
del this[2]
print(this)
this.clear()
print(this)

#loop in list
looplist = ["tanu","tinni","shuvra","toma","pori","rashmika"]
for x in looplist:
    print(x)

#ran len
for i in range(len(looplist)):
    print(i)

y = 0
while y<len(looplist):
    print(looplist[y])
    y = y+ 1


#list comprehension
num = [1,2,3,4,5]
for i in num:
    print(i*2)

double =[i*2 for i in num]
print(double)


#sort list
number = [3,4,9,1,2,5,6]
number.sort()
print(number)
cha = ["b","d","a"]
cha.sort()
print(cha)
cha.sort(reverse=True)
print(cha)


#copy a list
dip1 = cha.copy()
print(dip1)


#join two list
es = [1,2,3] 
di =[4,5,6]
join = es + di
print(join)

es.extend(di)
print(es)


#matrix
modulelist = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    5
]
print(modulelist[0][1])

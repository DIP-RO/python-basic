x = 0
while x<10:
    print("yes")
    x = x+1

fruit = ["apple", "banana" , "cherry"]
for n in fruit:
    if n == "banana":
        break
    print(n)


for x in range(9):
    if x == 3:
        break
    print(x)
dip = [1,2,3,4,5,6]
for v in range(len(dip)):
    if v == 4:
        continue
    print(v)
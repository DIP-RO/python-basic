import re
txt ="the train in spain"
x = re.findall("[a-m]",txt)
print(x)
pattern = "^the"
x = re.findall(pattern,txt)
print(x)
if x:
    print("yes")
else:
    print("no match")
#check all metachracters

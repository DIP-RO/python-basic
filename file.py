import os #for delete
#open
x = open("text.text","r")
print(x.read())

#create
wr = open("dipro.html","w")
wr.write("<p>subscribe<p/>")
wr = open("dipro.html","a")
wr.write("<p>subscribe<p/>")
#newlinw \n

#delete
os.remove("dipro.html")
#remove folder
os.rmdir("folderName")

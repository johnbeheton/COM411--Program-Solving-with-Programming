file = open("gaga.txt", "w")
for i in file.readlines():
   print(file.read())
file.close()
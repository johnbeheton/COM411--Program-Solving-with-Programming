f1 = open("john.txt")
f2 = open("harry,txt")

for i in range (3):
  print(f"\033[92mjohn: {f1.readline()}\033[0m anything" , end= "")
  print(f"\033[92mharry: {f1.readline()}\033[0m anything" , end= "")

  f1, f2.close()

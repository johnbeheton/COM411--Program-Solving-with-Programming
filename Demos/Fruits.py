def get_fruits():
  fruits = []
  print("How many fruits would you enter?")
  n = int(input())

  for i in range(4):
    print("Type in the next fruit:")
    fruits.append(input())

  
  #Print All
  print("Your fruits are{}".format(fruits))

  #Print few
  print(f"Sliced list: {fruits[0:5:2]}")

  #Print only few using negative Index
  print(f"Negative index: {fruits[-2]}")


get_fruits()    
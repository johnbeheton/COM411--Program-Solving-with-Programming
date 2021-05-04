import matplotlib.pyplot as plt
def coordinate():
  print("Please enter x value:")
  x=int(input())

  print("Please enter y value:")
  y=int(input())
  return(x,y)
def path():
  print("Retriving path...")
  x_value=[]
  y_value=[]
  for count in range(4):
    data=coordinate()
    x_value.append(data[0])
    y_value.append(data[1])
  return [x_value,y_value]
def run():
  value=path()
  plt.plot(value[0],value[1], "r--o")
  plt.show()
  
run()


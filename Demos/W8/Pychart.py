import matplotlib.pyplot as plt


x = ("Lithuania", "Romania", "Poland", "Bangladesh", "Brazil", "Columbia", "Other")
data = [2,17,1,2,2,2,6]


plt.pie(data, labels = x,shadow = True)

plt.show()
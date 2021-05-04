#Define empty list
fruits = []

#Define a list with items

vegetable = ["Carrot", "Peas"]

#Add to list

fruits.append("Apple")
fruits.append("Banana")
fruits.append("Tomatoe")
fruits.append("Cherry")

print(fruits)

#Remove item from list
fruits.remove("Banana")
print(fruits)

#Remove item by Index
del fruits[1]
print(fruits)

#Insert a value not at the end
fruits.insert(1, "Pineapple")
print(fruits)

#Access single element
print(fruits[0])
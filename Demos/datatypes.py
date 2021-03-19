print("What is your name")
#Variable is a container, which can store data for us in memory(string, intiger, float, bool)
name = input()
print("What is your age?")
age = int(input())
print("What is your bank balance?")
balance = float(input())

print("Welcome {}. Your are said to be {} years old. Your bank balance is £{:.2f}.".format(name, age, balance))

print("What is your name?")
n = input()
#print("Do you have a dog? (type True or False)")
#dog = input()
#bool is boolean - datatype store True/False

if len(n) >= 9: #allow 9 and greater
 print("You have a very long name!")
 print("Your name contains {} letters".format(len(n)))
elif len(n) > 6:
  print("Your name is a bit long Consider a nickname")
elif len(n) < 3:
  print("Your name is very short")
else:
  print("Your name is quite ok")
print("This is the END of the program!")
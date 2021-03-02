print("What is your name")
#Variable is a container, which can store data for us in memory(string, intiger, float, bool)
name = input()
print("What is your age?")
age = int(input())
print("What is your bank balance?")
balance = float(input())

print("Welcome {}. Your are said to be {} years old. Your bank balance is £{:.2f}.".format(name, age, balance))
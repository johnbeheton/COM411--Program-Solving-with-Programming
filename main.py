print("What is your name?")
n = input()
print("Do you have a dog? (type True or False)")
dog = input()
#bool is boolean - store True/False

if len(n) > 9 and dog == "True":
 print("You have a very long name!")
 print("Your name contains {} letters".format(len(n)))
else:
  print("Your name is quite ok")
print("This is the END of the program!")
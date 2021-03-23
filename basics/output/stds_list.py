  #Program that imitate a small database, this can:
  #insert new students
  #keep continually add
  #average mark of all students
  #find the maximum mark among all students


def generate_stds():
  print("Enter the name: ")
  name = input()
  print("Enter the grade: ")
  grade = int(input())
  return name, grade

def all_stds():
  all_students = []
  while True:
    all_students.append(generate_stds())
    print("To stop adding students, type 0")
    x = input()
    if x == '0':
      break
  return all_students  


def print_students(lista):
  for std in lista:
    print(f"{std[0]} earned a grade {std[1]}")


def avr_mark(lista):
  total=0
  for st in lista:
    total += std[1]
  return total/len(lista) 


print(avr_mark(all_stds()))  



import random

a = random.randint(1,12)
b = random.randint(1,12)

for i in range(0, 10):
  question = "What is " + a + " * " + b + "? "
  answer = input(question)
  print(type(answer))

  if answer == a * b:
    print ('Well done!')
  else:
    print("No.")

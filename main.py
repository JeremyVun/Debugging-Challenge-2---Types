import random

for i in range(0, 10):
  a = random.randint(1,12)
  b = random.randint(1,12)
  
  question = "What is " + a + " * " + b + "? "
  
  answer = input(question)

  if answer == a * b:
    print ('Well done!')
  else:
    print("No.")

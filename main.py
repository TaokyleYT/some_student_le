from some_student_le import *
import random
print("hello there! Lets play a game.")
op = ["+","-","*","/"][random.randint(0, 3)]
a = random.randint(2,1000)
if op=="/":
  b=a*random.randint(2,100)
elif op=="*":
  b = random.randint(2,100)
else:
  b = random.randint(2,1000)
ans = input("what is "+str(b)+op+str(a)+"? ")
if ans == str(eval(str(b)+op+str(a))):
  print("\x1b[42mYES YOU ARE CORRECT!!!\x1b[m")
else:
  print("\x1b[41mNO YOU ARE NOT CORRECT!!! The correct answer is",str(int(eval(str(b)+op+str(a))))+"\x1b[m")
input("Enter to exit ")
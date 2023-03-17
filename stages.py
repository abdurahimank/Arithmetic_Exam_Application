# Stage 2/4: Task generator
import random


x, y, oper = random.randint(2, 9), random.randint(2, 9), random.choice(["+", "-", "*"])
print(x, oper, y)
if int(input()) == eval(str(x) + oper + str(y)):
    print("Right!")
else:
    print("Wrong!")

# Project: Arithmetic Exam Application
# Stage 2/4: Task generator
import random


task = f"{random.randint(2, 9)} {random.choice(['+', '-', '*'])} {random.randint(2, 9)}"
print(task)
answer = int(input())
if answer == eval(task):
    print("Right!")
else:
    print("Wrong!")

# Project: Arithmetic Exam Application
# Stage 3/4: More tasks needed!
import random


mark = 0
no_qn = 5
while no_qn > 0:
    no_qn -= 1
    task = f"{random.randint(2, 9)} {random.choice(['+', '-', '*'])} {random.randint(2, 9)}"
    print(task)
    while True:
        try:
            answer = int(input())
            break
        except ValueError:
            print("Incorrect format.")
    if answer == eval(task):
        print("Right!")
        mark += 1
    else:
        print("Wrong!")
print(f"Your mark is {mark}/5.")

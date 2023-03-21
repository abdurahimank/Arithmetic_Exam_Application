# Stage 3/4: More tasks needed!
import random


game_count = 0
total_mark = 0
while game_count < 5:
    game_count += 1
    x, y, oper = random.randint(2, 9), random.randint(2, 9), random.choice(["+", "-", "*"])
    print(x, oper, y)
    while True:
        try:
            answer = int(input())
            break
        except (ValueError, TypeError):
            print("Incorrect format.")
    if answer == eval(str(x) + oper + str(y)):
        print("Right!")
        total_mark += 1
    else:
        print("Wrong!")
print(f"Your mark is {total_mark}/5.")


import random


def level_1():
    game_count = 0
    score = 0
    while game_count < 5:
        game_count += 1
        x, y, oper = random.randint(2, 9), random.randint(2, 9), random.choice(["+", "-", "*"])
        print(x, oper, y)
        while True:
            try:
                answer = int(input())
                break
            except (ValueError, TypeError):
                print("Wrong format! Try again.")
        if answer == eval(str(x) + oper + str(y)):
            print("Right!")
            score += 1
        else:
            print("Wrong!")
    return score


def level_2():
    game_count = 0
    score = 0
    while game_count < 5:
        game_count += 1
        x = random.randint(11, 29)
        print(x)
        while True:
            try:
                answer = int(input())
                break
            except (ValueError, TypeError):
                print("Wrong format! Try again.")
        if answer == x ** 2:
            print("Right!")
            score += 1
        else:
            print("Wrong!")
    return score


while True:
    level = input("""Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29""")
    if level == "1":
        total_mark = level_1()
    elif level == "2":
        total_mark = level_2()
    else:
        print("Incorrect format.")
        continue
    break
to_save = input(f"Your mark is {total_mark}/5. Would you like to save the result? Enter yes or no.")
if to_save in ["yes", "YES", "y", "Yes"]:
    name = input("What is your name?")
    file = open("results.txt", "at")
    file.write(f"{name}: {total_mark}/5 in level {level} "
               f"({'simple operations with numbers 2-9' if level == '1' else 'integral squares 11-29'})")
    file.close()
    print('The results are saved in "results.txt".')

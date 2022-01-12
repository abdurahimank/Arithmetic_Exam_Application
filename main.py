import random


def level_2():
    num = random.choice([j for j in range(11, 30)])
    print(num)
    answer = user_answer()
    correct = num ** 2
    print("Right!" if answer == correct else "Wrong!")
    return 1 if answer == correct else 0


def level_1():
    num_list = [j for j in range(2, 10)]
    operator_list = ["+", "-", "*"]
    for _ in range(5):
        num_1 = random.choice(num_list)
        num_2 = random.choice(num_list)
        operation = random.choice(operator_list)
        print(num_1, operation, num_2)
        answer = user_answer()
        if operation == "+":
            correct = num_1 + num_2
        elif operation == "-":
            correct = num_1 - num_2
        elif operation == "*":
            correct = num_1 * num_2
        else:
            correct = num_1 / num_2
        print("Right!" if answer == correct else "Wrong!")
        return 1 if answer == correct else 0


def user_answer():
    while True:
        x = input()
        if len(x) > 0 and (x.isdigit() or (x[0] == "-" and x[1:].isdigit())):
            break
        else:
            print("Wrong format! Try again.")
            continue
    return int(x)


while True:
    difficulty_level = int(input("""Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29\n"""))
    if difficulty_level != 1 and difficulty_level != 2:
        print("Incorrect format.")
        continue
    else:
        break
score = 0
for i in range(5):
    if difficulty_level == 1:
        score += level_1()
    else:
        score += level_2()
save_status = input(f"Your mark is {score}/5. Would you like to save the result? Enter yes or no.")
if save_status in ['yes', 'YES', 'y', 'Yes']:
    user_name = input("What is your name?")
    file_1 = open("results.txt", "a")
    if difficulty_level == 1:
        file_1.write(f"{user_name}: {score}/5 in level 1 (simple operations with numbers 2-9).")
    else:
        file_1.write(f"{user_name}: {score}/5 in level 2 (integral squares 11-29).")
    file_1.close()
    print('The results are saved in "results.txt".')

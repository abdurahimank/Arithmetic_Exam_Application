import random

mark = 0
while True:
    level = input('''Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29\n''')
    if level == '1' or level == '2':
        break
    else:
        print('Incorrect format.')
for _ in range(5):
    if level == '1':
        value_1 = random.randint(2, 9)
        value_2 = random.randint(2, 9)
        operation = random.choice(['*', '+', '-'])
        print(str(value_1) + operation + str(value_2))
        correct_answer = eval(str(value_1) + operation + str(value_2))
        description = 'level 1 (simple operations with numbers 2-9)'
    if level == '2':
        value_1 = random.randint(11, 29)
        print(value_1)
        correct_answer = value_1 ** 2
        description = 'level 2 (integral squares 11-29)'

    while True:
        try:
            player_answer = int(input())
            break
        except ValueError:
            print('Incorrect format.')
            continue
    if player_answer == correct_answer:
        print('Right!')
        mark += 1
    else:
        print('Wrong!')
save = input(f'Your mark is {mark}/5. Would you like to save the result? Enter yes or no.\n')
if save in ['yes', 'YES', 'y', 'Yes']:
    name = input('What is your name?\n')
    file = open('results.txt', 'a', encoding='utf_8')
    file.write(f'{name}: {mark}/5 in {description}.')
    file.close()
    print('The results are saved in "results.txt".')
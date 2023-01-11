variant_winner = [
    ['00', '10', '20'], # first vertical
    ['01', '11', '21'], # second vertical
    ['02', '12', '22'], # third vertical

    ['00', '01', '02'], # first horizontal
    ['10', '11', '12'], # second horizontal
    ['20', '21', '22'], # third horizontal

    ['00', '11', '22'], # left top  diagonal
    ['02', '11', '20'], # right top diagonal
]

user_choose = {
    'x': [],
    '0': []
}


table = [
    # 0    1    2
    ['-', '-', '-'],  # 0
    ['-', '-', '-'],  # 1
    ['-', '-', '-'],  # 2
]


def print_table(table):
    print(*[' ', 0, 1, 2])
    for index, row in enumerate(table):
        print(index, *row)


def check_winner(user_choose, variant_winner):
    for winner in variant_winner:
        if len([x in winner for x in user_choose]) == 3:
            return True
    return False


def check_user_input(user_input):
    if len(user_input) != 2:
        print('You can input only two numbers')
        return False
    if user_input in user_choose['x'] or user_input in user_choose['0']:
        print('This cell is already taken')
        return False
    if not user_input.isdigit():
        print('You can input only numbers')
        return False
    return True


print_table(table)

player = 'x'
count_step = 1
while count_step <= 9:
    user = input(f'Enter {player}: ')
    check_input = check_user_input(user)
    if not check_input:
        print('Your coordinates are wrong. Try again...')
        continue
    user_choose[player].append(user)

    first = int(user[0])
    second = int(user[1])

    table[first][second] = player
    print_table(table)

    check = check_winner(user_choose[player], variant_winner)
    if check:
        print('The winner player ', player)
        break

    player = '0' if player == 'x' else 'x'
    count_step += 1








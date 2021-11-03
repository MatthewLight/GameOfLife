import copy

initial_board_state = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]


def is_alive(cell):
    if cell:
        return True
    else:
        return False


def get_amount_of_live_neighbours(state, i, j):
    neighbours = []
    for row_add in range(-1, 2):
        new_row = j + row_add
        if 0 <= new_row <= len(state)-1:
            for col_add in range(-1, 2):
                new_col = i + col_add
                if 0 <= new_col <= len(state)-1:
                    if new_col == i and new_row == j:
                        continue
                    neighbours.append(state[new_col][new_row])
    return sum(neighbours)


def die_or_not_to_die(cell, state, i, j):
    alive_neighbours_amount = get_amount_of_live_neighbours(state, i, j)

    if is_alive(cell):
        if alive_neighbours_amount < 2:
            return 0
        elif alive_neighbours_amount == 2 or alive_neighbours_amount == 3:
            return 1
        elif alive_neighbours_amount > 3:
            return 0
    else:
        if alive_neighbours_amount == 3:
            return 1
        else:
            return cell


def transform_cell_state(state, i, j):
    return die_or_not_to_die(state[i][j], state, i, j)


def transform_state(state):
    transformed_state = copy.deepcopy(state)
    for i in range(len(initial_board_state)):
        for j in range(len(initial_board_state[i])):
            transformed_state[i][j] = transform_cell_state(state, i, j)

    return transformed_state


def draw_board(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            print(state[i][j], end='\t')
        print('\n')
    print('===============================Next_Iteration================================\n')


def main(initial_state, iterations):
    state = copy.deepcopy(initial_state)
    draw_board(state)
    for i in range(0, iterations):
        state = transform_state(state)
        draw_board(state)


main(initial_board_state, 10)

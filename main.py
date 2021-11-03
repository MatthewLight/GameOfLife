import copy

initial_board_state = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

state_copy = copy.deepcopy(initial_board_state)


def is_alive(cell):
    if cell:
        return True
    else:
        return False


def get_amount_of_live_neighbours(matrix, row, column):
    result = []
    for row_add in range(-1, 2):
        new_row = column + row_add
        if 0 <= new_row <= len(matrix)-1:
            for colAdd in range(-1, 2):
                new_col = row + colAdd
                if 0 <= new_col <= len(matrix)-1:
                    if new_col == row and new_row == column:
                        continue
                    result.append(matrix[new_col][new_row])
    return sum(result)


def die_or_not_to_die(cell, matrix, x, y):
    alive_neighbours = get_amount_of_live_neighbours(matrix, x, y)
    if is_alive(cell):
        if alive_neighbours < 2:
            return 0  # dies
        elif alive_neighbours == 2 or alive_neighbours == 3:
            return 1  # remains alive
        elif alive_neighbours > 3:
            return 0  # dies
    else:
        if alive_neighbours == 3:
            return 1  # become alive
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
    print('===========Next_Iteration============\n')


def main(initial_state, iterations):
    state = copy.deepcopy(initial_state)
    draw_board(state)
    for i in range(0, iterations):
        state = transform_state(state)
        draw_board(state)


main(initial_board_state, 10)

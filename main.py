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
    return cell == 1


def get_amount_of_alive_neighbours(state, row, column):
    neighbours = []
    for column_add in range(-1, 2):
        current_column = column + column_add
        if 0 <= current_column <= len(state)-1:
            for row_add in range(-1, 2):
                current_row = row + row_add
                if 0 <= current_row <= len(state)-1:
                    if current_row == row and current_column == column:
                        continue
                    neighbours.append(state[current_row][current_column])
    return sum(neighbours)


def transform_alive_cell(neighbours):
    return 1 if 1 < neighbours < 4 else 0


def transform_dead_cell(neighbours):
    return 1 if neighbours == 3 else 0


def transform_cell_state(state, row, column):
    alive_neighbours = get_amount_of_alive_neighbours(state, row, column)
    cell = state[row][column]

    return transform_alive_cell(alive_neighbours) \
        if is_alive(cell) \
        else transform_dead_cell(alive_neighbours)


def transform_state(state):
    transformed_state = copy.deepcopy(state)
    for row in range(len(initial_board_state)):
        for column in range(len(initial_board_state[row])):
            transformed_state[row][column] = transform_cell_state(state, row, column)

    return transformed_state


def draw_board(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            print(state[i][j], end='\t')
        print('\n')
    print('===============================End_of_Iteration================================\n')


def main(initial_state, iterations):
    state = copy.deepcopy(initial_state)
    draw_board(state)
    for i in range(iterations):
        state = transform_state(state)
        draw_board(state)


main(initial_board_state, 10)

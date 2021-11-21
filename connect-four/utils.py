import functools


def pretty_print_board(board, col_height, num_cols, p1="X", p2="O"):
    """
    Pretty print the Connect4 board
    """
    players = {
        1: p1,
        -1: p2,
        0: " "
    }

    print(f"P1: {p1}\tP2: {p2}", end='\n')

    # print header
    print("  ╔" + "═════╦" * (num_cols - 1) + "═════╗")
    for y in range(col_height):
        if y > 0:
            print("  ╠" + "═════╬" * (num_cols - 1) + "═════╣")
        for x in range(num_cols):
            if x == 0:
                print(f"{col_height - y - 1} ║", end="")

            print(
                f"  {players[board[x, col_height - y - 1]]}  " + "║", end="")
        print()

    print("  ╚" + "═════╩" * (num_cols - 1) + "═════╝")
    print("   " + "".join(map(lambda i: f"  {i}   ", range(num_cols))) + " ")


def counted(f):
    """
    Function decorator that counts the number of invokations
    of the wrapped function
    """
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        wrapped.calls += 1
        return f(*args, **kwargs)
    wrapped.calls = 0
    return wrapped

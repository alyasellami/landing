def display_map(height, width, joueur):
    for y in range(height):
        for x in range(width):
            if joueur == (x, y):
                print("[ X ] ", end="")
            else:
                print("[   ] ", end="")
        print()


def run_game():
    WIDTH = 8
    HEIGHT = 6
    position = (0, 0)

    while True:
        display_map(WIDTH, HEIGHT, position)

        ordre = input("Gauche, Droite, Haut, Bas, Quitter ? ")
        if ordre.lower().startswith("quit"):
            break

        if ordre.lower().startswith("g"):
            if position[0] > 0:
                position = (position[0] - 1, position[1])

        elif ordre.lower().startswith("d"):
            if position[0] < WIDTH - 1:
                position = (position[0] + 1, position[1])

        elif ordre.lower().startswith("h"):
            if position[1] > 0:
                position = (position[0], position[1] - 1)

        elif ordre.lower().startswith("b"):
            if position[1] < HEIGHT - 1:
                position = (position[0], position[1] + 1)


if __name__ == "__main__":
    run_game()

import random


def transfer_item(source, target, item):
    if item in source:
        source.remove(item)
        target.append(item)
    return source, target


def run_game(available_items):
    ground = random.choices(available_items, k=5)
    inventory = []
    while True:
        print("sol :", ground, "inventaire :", inventory)
        ordre = input(
            "Voulez vous PRENDRE <objet>, POSER <objet> ou QUITTER > "
        ).split()

        if ordre[0].lower().startswith("quit"):
            break

        if ordre[0].lower().startswith("pre"):
            ground, inventory = transfer_item(ground, inventory, ordre[1])
        elif ordre[0].lower().startswith("pos"):
            inventory, ground = transfer_item(inventory, ground, ordre[1])


if __name__ == "__main__":
    run_game(["clé", "arc", "marteau", "table", "porte", "souris", "fromage"])

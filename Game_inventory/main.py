from inventory import Inventory


def get_str(message: str) -> str:
    return input(f'{message}:\n')


def get_int(message: str) -> int:
    return int(input(f'{message}:\n'))


def main():
    inventory = Inventory()
    a = 0
    while a != 3:
        print('Witaj w ekwipunku gracza, wybierz opcję')
        print('------------------')
        print(inventory)
        print('------------------')
        print('1 - dodaj przedmiot do Twojego ekwipunku')
        print('2 - usuń przedmiot z Twojego ekwipunku')
        print('3 - usuń wszystkie przedmioty')
        a = int(input())
        match a:
            case 1:
                your_name = get_str('Podaj przedmiot')
                your_number = get_int('Podaj ilość')
                inventory.add_item(your_name, your_number)
            case 2:
                your_name = get_str('Podaj przedmiot')
                your_number = get_int('Podaj ilość')
                inventory.remove_item(your_name, your_number)
            case 3:
                inventory.clear_inventory()


if __name__ == "__main__":
    main()

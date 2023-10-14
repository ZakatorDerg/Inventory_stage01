"""
    A class to manage an inventory.

    Attributes
    ----------
    items:  dict[str, int]
        inventory

    Methods
    -------
    __init__()
        creates an empty inventory
    add_item(item: str, quantity: int)
        adds certain amount of the item into the inventory
    remove_item(item: str, quantity: int)
        removes certain amount of the item from the inventory
    clear_inventory()
        empties the inventory
    __str__()
        defines how the objected will be printed out
"""


from dataclasses import dataclass
from typing import Self


class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item: str, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError('Wrong Value!')
        self.items[item] = quantity

    def remove_item(self, item: str, quantity: int) -> None:
        if quantity < 0:
            raise ValueError('Nie ma XD')
        if not self.items:
            print('Inventory is empty')
        elif item not in self.items.keys():
            print('There is no item in inventory')
        else:
            self.items[item] -= quantity
            if self.items[item] <= 0:
                self.items.pop(item)

    def clear_inventory(self) -> None:
        self.items.clear()

    def __str__(self):
        return f'{self.items}'








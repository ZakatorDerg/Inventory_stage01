"""
Plik ten zajmuje się...
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








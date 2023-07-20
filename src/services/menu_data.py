import csv

from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        new_dict = {}

        with open(source_path, encoding="utf-8") as file:
            _, *menu_data = csv.reader(file)

            for dish, price, ingredient, amount in menu_data:
                new_dish = Dish(dish, float(price))
                new_ingredient = Ingredient(ingredient)
                if dish not in new_dict:
                    new_dict[dish] = new_dish

                new_dict[dish].add_ingredient_dependency(
                    new_ingredient, int(amount)
                )

            self.dishes.update(new_dict.values())

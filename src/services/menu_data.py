import csv
from models.ingredient import Ingredient
from models.dish import Dish


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = self.load_menu_data(source_path)

    def load_menu_data(self, source_path):
        dish_create = set()
        with open(source_path, "r") as file:
            dishes_reader = csv.DictReader(file)
            for item in dishes_reader:
                dish_name = item["dish"]
                price = float(item["price"])
                ingredients_name = item["ingredient"]
                recipe_amount = float(item["recipe_amount"])

                # verifica se o prato já existe
                existing_dish = next((
                        d for d in dish_create if d.name == dish_name), None)
                if existing_dish:
                    existing_dish.add_ingredient_dependency(
                        Ingredient(ingredients_name), recipe_amount
                    )
                else:
                    new_dish = Dish(dish_name, price)
                    new_dish.add_ingredient_dependency(
                        Ingredient(ingredients_name), recipe_amount
                    )
                    dish_create.add(new_dish)
        return dish_create

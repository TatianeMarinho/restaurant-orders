from src.models.dish import Dish  # noqa: F401, E261, E501

import pytest  # noqa: F401, E261, E501


# Req 2
def test_dish():
    dish_one = Dish("Salada", 19.99)
    dish_two = Dish("lasanha berinjela", 27.00)

    assert dish_one.name == "Salada"
    assert dish_two.name == "lasanha berinjela"
    assert dish_one.price == 19.99
    assert dish_two.price == 27.00
    assert dish_one.recipe == {}
    assert dish_two.recipe == {}
    assert repr(dish_one) == "Dish('Salada', R$19.99)"
    assert repr(dish_two) == "Dish('lasanha berinjela', R$27.00)"
    assert dish_one == dish_one
    assert dish_two != dish_one
    assert hash(dish_one) == hash(dish_one)
    assert hash(dish_two) != hash(dish_one)
    assert dish_one.get_restrictions() == set()
    assert dish_two.get_restrictions() == set()
    assert dish_one.get_ingredients() == set()
    assert dish_two.get_ingredients() == set()
    with pytest.raises(TypeError):
        Dish("Salada", "alface")
    with pytest.raises(TypeError):
        Dish("lasanha berinjela", "alface")
    with pytest.raises(ValueError):
        Dish("Salada", -19.99)
    with pytest.raises(ValueError):
        Dish("lasanha berinjela", -27.00)

    ingredient_one = "alface"
    ingredient_two = "cebola"
    ingredient_three = "tomate"
    dish_one.add_ingredient_dependency(ingredient_one, 4.50)
    assert dish_one.recipe == {ingredient_one: 4.50}
    dish_one.add_ingredient_dependency(ingredient_two, 2.00)
    dish_one.add_ingredient_dependency(ingredient_three, 3.00)
    assert dish_one.recipe == {
        ingredient_one: 4.50,
        ingredient_two: 2.00,
        ingredient_three: 3.00
    }

from src.models.ingredient import Ingredient, Restriction # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient_one = Ingredient("queijo mussarela")
    expected_restrictions = {
       Restriction.LACTOSE,
       Restriction.ANIMAL_DERIVED
    }
    assert ingredient_one.name == "queijo mussarela"
    assert ingredient_one.restrictions == expected_restrictions

    ingredient_two = Ingredient("alface")
    ingredient_three = Ingredient("alface")
    assert ingredient_two.name == "alface"
    assert ingredient_three.name == "alface"
    assert ingredient_two.restrictions == set()
    assert ingredient_two != ingredient_one
    assert ingredient_two == ingredient_three
    assert repr(ingredient_two) == "Ingredient('alface')"
    assert repr(ingredient_one) == "Ingredient('queijo mussarela')"
    assert hash(ingredient_two) == hash(ingredient_three)
    assert hash(ingredient_two) != hash(ingredient_one)

from src.models.ingredient import Ingredient, Restriction, restriction_map  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient_one = Ingredient("queijo mussarela")
    expected_restrictions = {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED
    }
    assert ingredient_one.name == "queijo mussarela"
    assert ingredient_one.restrictions == expected_restrictions

    ingredient_two = Ingredient("bacon")
    expected_restrictions_dois = {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT
    }
    assert ingredient_two.name == "bacon"
    assert ingredient_two.restrictions == expected_restrictions_dois
    assert ingredient_one != ingredient_two
    assert repr(ingredient_one) == "Ingredient('queijo mussarela')"
    assert repr(ingredient_two) == "Ingredient('bacon')"
    assert hash(ingredient_one) != hash(ingredient_two)

    ingredient_tree = Ingredient("alface")
    ingredient_four = Ingredient("alface")
    assert ingredient_tree.name == "alface"
    assert ingredient_tree.restrictions == set()
    assert repr(ingredient_tree) == "Ingredient('alface')"
    assert hash(ingredient_tree) == hash(ingredient_four)

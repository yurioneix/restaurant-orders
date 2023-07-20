import pytest
from src.models.dish import Dish, Ingredient
from src.models.ingredient import Restriction  # noqa: F401, E261, E501


# Req 2
def test_dish():
    with pytest.raises(TypeError):
        Dish("lasanha", "15")

    with pytest.raises(ValueError):
        Dish("bolo", 0)

    dish_1 = Dish("miojo", 3)
    assert dish_1.name == "miojo"
    assert dish_1.price == 3
    assert repr(dish_1) == "Dish('miojo', R$3.00)"

    dish_2 = Dish("miojo", 3)
    assert dish_1 == dish_2

    assert dish_1.__hash__() == dish_2.__hash__()

    dish_3 = Dish("carne assada", 30)
    assert dish_1.__hash__() != dish_3.__hash__()

    carne = Ingredient("carne")

    dish_3.add_ingredient_dependency(carne, 2)
    assert dish_3.recipe == {Ingredient("carne"): 2}

    assert dish_3.get_ingredients() == {carne}

    assert dish_3.get_restrictions() == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }

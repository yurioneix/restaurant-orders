from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient_1 = Ingredient("farinha")

    assert ingredient_1.name == "farinha"
    assert ingredient_1.restrictions == {Restriction.GLUTEN}

    ingredient_2 = Ingredient("ovo")
    assert not ingredient_1 == ingredient_2
    assert repr(ingredient_2) == "Ingredient('ovo')"

    ingredient_3 = Ingredient("farinha")
    assert ingredient_1.__hash__() == ingredient_3.__hash__()
    assert ingredient_2.__hash__() != ingredient_1.__hash__()
    assert ingredient_3 == ingredient_1

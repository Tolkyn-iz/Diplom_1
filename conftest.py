import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def burger():
    """Фикстура: создаёт бургер для каждого теста"""
    return Burger()


@pytest.fixture
def mock_bun():
    """Фикстура: мок-булка"""
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100.0
    return bun


@pytest.fixture
def mock_sauce():
    """Фикстура: мок-соус"""
    sauce = Mock(spec=Ingredient)
    sauce.get_name.return_value = "hot sauce"
    sauce.get_price.return_value = 50.0
    sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return sauce


@pytest.fixture
def mock_filling():
    """Фикстура: мок-начинка"""
    filling = Mock(spec=Ingredient)
    filling.get_name.return_value = "cutlet"
    filling.get_price.return_value = 200.0
    filling.get_type.return_value = INGREDIENT_TYPE_FILLING
    return filling
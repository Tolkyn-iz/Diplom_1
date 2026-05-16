import pytest
from unittest.mock import Mock, patch, MagicMock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestBurger:
    """Тесты для класса Burger"""

    def setup_method(self):
        """Создание экземпляра Burger перед каждым тестом"""
        self.burger = Burger()
        
        # Создаем моки для булочек
        self.mock_bun = Mock(spec=Bun)
        self.mock_bun.get_name.return_value = "black bun"
        self.mock_bun.get_price.return_value = 100.0
        
        # Создаем моки для ингредиентов
        self.mock_ingredient1 = Mock(spec=Ingredient)
        self.mock_ingredient1.get_name.return_value = "hot sauce"
        self.mock_ingredient1.get_price.return_value = 100.0
        self.mock_ingredient1.get_type.return_value = INGREDIENT_TYPE_SAUCE
        
        self.mock_ingredient2 = Mock(spec=Ingredient)
        self.mock_ingredient2.get_name.return_value = "cutlet"
        self.mock_ingredient2.get_price.return_value = 200.0
        self.mock_ingredient2.get_type.return_value = INGREDIENT_TYPE_FILLING
        
        self.mock_ingredient3 = Mock(spec=Ingredient)
        self.mock_ingredient3.get_name.return_value = "sausage"
        self.mock_ingredient3.get_price.return_value = 300.0
        self.mock_ingredient3.get_type.return_value = INGREDIENT_TYPE_FILLING

    # Тесты для set_buns
    def test_set_buns(self):
        """Тест установки булочки"""
        self.burger.set_buns(self.mock_bun)
        assert self.burger.bun == self.mock_bun

    def test_set_buns_should_set_bun_correctly(self):
        """Тест проверки корректной установки булочки через методы"""
        self.burger.set_buns(self.mock_bun)
        assert self.burger.bun.get_name() == "black bun"
        assert self.burger.bun.get_price() == 100.0

    # Тесты для add_ingredient
    def test_add_ingredient(self):
        """Тест добавления одного ингредиента"""
        self.burger.add_ingredient(self.mock_ingredient1)
        assert len(self.burger.ingredients) == 1
        assert self.burger.ingredients[0] == self.mock_ingredient1

    def test_add_multiple_ingredients(self):
        """Тест добавления нескольких ингредиентов"""
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        self.burger.add_ingredient(self.mock_ingredient3)
        
        assert len(self.burger.ingredients) == 3
        assert self.burger.ingredients[0] == self.mock_ingredient1
        assert self.burger.ingredients[1] == self.mock_ingredient2
        assert self.burger.ingredients[2] == self.mock_ingredient3

    # Тесты для remove_ingredient
    def test_remove_ingredient_by_index(self):
        """Тест удаления ингредиента по индексу"""
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        self.burger.add_ingredient(self.mock_ingredient3)
        
        self.burger.remove_ingredient(1)
        
        assert len(self.burger.ingredients) == 2
        assert self.burger.ingredients[0] == self.mock_ingredient1
        assert self.burger.ingredients[1] == self.mock_ingredient3

    def test_remove_first_ingredient(self):
        """Тест удаления первого ингредиента"""
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        
        self.burger.remove_ingredient(0)
        
        assert len(self.burger.ingredients) == 1
        assert self.burger.ingredients[0] == self.mock_ingredient2

    def test_remove_last_ingredient(self):
        """Тест удаления последнего ингредиента"""
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        
        self.burger.remove_ingredient(1)
        
        assert len(self.burger.ingredients) == 1
        assert self.burger.ingredients[0] == self.mock_ingredient1

    # Тесты для move_ingredient
    def test_move_ingredient_forward(self):
        """Тест перемещения ингредиента вперед"""
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        self.burger.add_ingredient(self.mock_ingredient3)
        
        # Перемещаем ингредиент с индексом 2 на позицию 1
        self.burger.move_ingredient(2, 1)
        
        assert len(self.burger.ingredients) == 3
        assert self.burger.ingredients[0] == self.mock_ingredient1
        assert self.burger.ingredients[1] == self.mock_ingredient3
        assert self.burger.ingredients[2] == self.mock_ingredient2

    def test_move_ingredient_backward(self):
        """Тест перемещения ингредиента назад"""
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        self.burger.add_ingredient(self.mock_ingredient3)
        
        # Перемещаем ингредиент с индексом 0 на позицию 2
        self.burger.move_ingredient(0, 2)
        
        assert len(self.burger.ingredients) == 3
        assert self.burger.ingredients[0] == self.mock_ingredient2
        assert self.burger.ingredients[1] == self.mock_ingredient3
        assert self.burger.ingredients[2] == self.mock_ingredient1

    def test_move_ingredient_to_same_position(self):
        """Тест перемещения ингредиента на ту же позицию"""
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        
        self.burger.move_ingredient(1, 1)
        
        assert len(self.burger.ingredients) == 2
        assert self.burger.ingredients[0] == self.mock_ingredient1
        assert self.burger.ingredients[1] == self.mock_ingredient2

    # Тесты для get_price
    def test_get_price_without_bun_and_ingredients(self):
        """Тест получения цены без булочки и ингредиентов"""
        self.burger.set_buns(self.mock_bun)
        price = self.burger.get_price()
        
        expected_price = self.mock_bun.get_price() * 2
        assert price == expected_price

    def test_get_price_with_bun_only(self):
        """Тест получения цены только с булочкой"""
        self.burger.set_buns(self.mock_bun)
        
        price = self.burger.get_price()
        
        assert price == 200.0  # 100 * 2

    def test_get_price_with_bun_and_ingredients(self):
        """Тест получения цены с булочкой и ингредиентами"""
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_ingredient1)  # price = 100
        self.burger.add_ingredient(self.mock_ingredient2)  # price = 200
        
        price = self.burger.get_price()
        
        assert price == 200.0 + 100.0 + 200.0  # 500

    @pytest.mark.parametrize("bun_price,ingredient_prices,expected", [
        (50, [10, 20], 50*2 + 10 + 20),  # 130
        (100, [50, 50, 50], 100*2 + 150),  # 350
        (200, [], 200*2),  # 400
        (75.5, [25.25, 30.75], 75.5*2 + 56.0),  # 207.0
    ])
    def test_get_price_with_params(self, bun_price, ingredient_prices, expected):
        """Параметризованный тест расчета цены с разными значениями"""
        mock_bun = Mock(spec=Bun)
        mock_bun.get_price.return_value = bun_price
        self.burger.set_buns(mock_bun)
        
        for price in ingredient_prices:
            mock_ingredient = Mock(spec=Ingredient)
            mock_ingredient.get_price.return_value = price
            self.burger.add_ingredient(mock_ingredient)
        
        assert self.burger.get_price() == expected

    # Тесты для get_receipt
    def test_get_receipt_with_bun_only(self):
        """Тест получения чека только с булочкой"""
        self.burger.set_buns(self.mock_bun)
        
        receipt = self.burger.get_receipt()
        
        expected_lines = [
            "(==== black bun ====)",
            "(==== black bun ====)\n",
            "Price: 200.0"
        ]
        expected_receipt = "\n".join(expected_lines)
        
        assert receipt == expected_receipt

    def test_get_receipt_with_bun_and_ingredients(self):
        """Тест получения чека с булочкой и ингредиентами"""
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        
        receipt = self.burger.get_receipt()
        
        expected_lines = [
            "(==== black bun ====)",
            "= sauce hot sauce =",
            "= filling cutlet =",
            "(==== black bun ====)\n",
            "Price: 500.0"
        ]
        expected_receipt = "\n".join(expected_lines)
        
        assert receipt == expected_receipt

    def test_get_receipt_ingredient_type_format(self):
        """Тест форматирования типа ингредиента в чеке"""
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_ingredient1)  # SAUCE
        self.burger.add_ingredient(self.mock_ingredient2)  # FILLING
        
        receipt_lines = self.burger.get_receipt().split('\n')
        
        # Проверяем, что тип ингредиента в нижнем регистре
        assert "= sauce hot sauce =" in receipt_lines
        assert "= filling cutlet =" in receipt_lines

    def test_get_receipt_order_of_elements(self):
        """Тест порядка элементов в чеке"""
        self.burger.set_buns(self.mock_bun)
        self.burger.add_ingredient(self.mock_ingredient1)
        self.burger.add_ingredient(self.mock_ingredient2)
        
        receipt = self.burger.get_receipt()
        
        # Проверяем, что сначала идет верхняя булочка
        assert receipt.startswith("(==== black bun ====)")
        # Затем ингредиенты
        assert "= sauce hot sauce =" in receipt
        assert "= filling cutlet =" in receipt
        # Потом нижняя булочка
        assert "(==== black bun ====)\n" in receipt
        # И в конце цена
        assert receipt.endswith("Price: 500.0")

    # Интеграционные тесты с реальными объектами
    def test_integration_with_real_bun(self):
        """Интеграционный тест с реальной булочкой"""
        real_bun = Bun("white bun", 200)
        self.burger.set_buns(real_bun)
        
        assert self.burger.bun.get_name() == "white bun"
        assert self.burger.bun.get_price() == 200
        assert self.burger.get_price() == 400

    def test_integration_with_real_ingredient(self):
        """Интеграционный тест с реальным ингредиентом"""
        real_bun = Bun("black bun", 100)
        real_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "cheese sauce", 150)
        
        self.burger.set_buns(real_bun)
        self.burger.add_ingredient(real_ingredient)
        
        assert self.burger.get_price() == 350
        
        receipt = self.burger.get_receipt()
        assert "= sauce cheese sauce =" in receipt

    # Тест комплексной последовательности операций (ИСПРАВЛЕН)
    def test_complex_sequence_operations(self):
        """Тест комплексной последовательности операций"""
        self.burger.set_buns(self.mock_bun)  # bun price = 100
        self.burger.add_ingredient(self.mock_ingredient1)  # sauce, price=100
        self.burger.add_ingredient(self.mock_ingredient2)  # cutlet, price=200
        self.burger.add_ingredient(self.mock_ingredient3)  # sausage, price=300

        # Проверяем начальное состояние
        assert len(self.burger.ingredients) == 3
        assert self.burger.ingredients[0] == self.mock_ingredient1
        assert self.burger.ingredients[1] == self.mock_ingredient2
        assert self.burger.ingredients[2] == self.mock_ingredient3

        # Перемещаем ингредиент с индексом 2 (sausage) на позицию 0
        self.burger.move_ingredient(2, 0)
        # Теперь порядок: [sausage, sauce, cutlet]
        assert self.burger.ingredients[0] == self.mock_ingredient3
        assert self.burger.ingredients[1] == self.mock_ingredient1
        assert self.burger.ingredients[2] == self.mock_ingredient2

        # Удаляем ингредиент с индексом 1 (sauce)
        self.burger.remove_ingredient(1)
        # Теперь порядок: [sausage, cutlet]
        assert len(self.burger.ingredients) == 2
        assert self.burger.ingredients[0] == self.mock_ingredient3  # sausage
        assert self.burger.ingredients[1] == self.mock_ingredient2  # cutlet

        # Проверяем цену: булка (100*2) + sausage(300) + cutlet(200) = 200 + 300 + 200 = 700
        price = self.burger.get_price()
        expected_price = self.mock_bun.get_price() * 2 + self.mock_ingredient3.get_price() + self.mock_ingredient2.get_price()
        assert price == expected_price  # 700

    # Тест проверки порядка ингредиентов после нескольких операций
    def test_ingredient_order_after_multiple_operations(self):
        """Тест порядка ингредиентов после нескольких операций"""
        self.burger.set_buns(self.mock_bun)
        
        ingredients = [self.mock_ingredient1, self.mock_ingredient2, self.mock_ingredient3]
        for ing in ingredients:
            self.burger.add_ingredient(ing)
        
        # Перемещаем последний в начало
        self.burger.move_ingredient(2, 0)
        assert self.burger.ingredients[0] == self.mock_ingredient3
        assert self.burger.ingredients[1] == self.mock_ingredient1
        assert self.burger.ingredients[2] == self.mock_ingredient2
        
        # Перемещаем первый в конец
        self.burger.move_ingredient(0, 2)
        assert self.burger.ingredients[0] == self.mock_ingredient1
        assert self.burger.ingredients[1] == self.mock_ingredient2
        assert self.burger.ingredients[2] == self.mock_ingredient3
        
        # Удаляем средний
        self.burger.remove_ingredient(1)
        assert len(self.burger.ingredients) == 2
        assert self.burger.ingredients[0] == self.mock_ingredient1
        assert self.burger.ingredients[1] == self.mock_ingredient3
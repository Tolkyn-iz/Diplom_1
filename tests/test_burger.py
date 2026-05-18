from praktikum.burger import Burger


class TestBurger:
    """Тесты для класса Burger"""

    def test_set_buns(self, burger, mock_bun):
        """Установка булки в бургер"""
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_set_buns_updates_bun_reference(self, burger, mock_bun):
        """Проверка что булка установлена корректно"""
        burger.set_buns(mock_bun)
        assert burger.bun is not None
        assert burger.bun.get_name() == "black bun"

    def test_add_ingredient_single(self, burger, mock_sauce):
        """Добавление одного ингредиента"""
        burger.add_ingredient(mock_sauce)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_sauce

    def test_add_ingredient_multiple(self, burger, mock_sauce, mock_filling):
        """Добавление нескольких ингредиентов"""
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        assert len(burger.ingredients) == 2

    def test_remove_ingredient_by_index(self, burger, mock_sauce, mock_filling):
        """Удаление ингредиента по индексу"""
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_filling

    def test_remove_ingredient_last(self, burger, mock_sauce, mock_filling):
        """Удаление последнего ингредиента"""
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.remove_ingredient(1)
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == mock_sauce

    def test_move_ingredient_forward(self, burger, mock_sauce, mock_filling):
        """Перемещение ингредиента вперёд"""
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == mock_filling
        assert burger.ingredients[1] == mock_sauce

    def test_move_ingredient_backward(self, burger, mock_sauce, mock_filling):
        """Перемещение ингредиента назад"""
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_filling
        assert burger.ingredients[1] == mock_sauce

    def test_get_price_only_bun(self, burger, mock_bun):
        """Цена бургера только с булкой (верх + низ)"""
        burger.set_buns(mock_bun)
        assert burger.get_price() == 200.0

    def test_get_price_with_one_ingredient(self, burger, mock_bun, mock_sauce):
        """Цена бургера с булкой и одним ингредиентом"""
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        assert burger.get_price() == 250.0

    def test_get_price_with_multiple_ingredients(self, burger, mock_bun, mock_sauce, mock_filling):
        """Цена бургера с булкой и несколькими ингредиентами"""
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        assert burger.get_price() == 450.0

    def test_get_receipt_without_ingredients(self, burger, mock_bun):
        """Рецепт бургера без ингредиентов"""
        burger.set_buns(mock_bun)
        receipt = burger.get_receipt()
        assert "(==== black bun ====)" in receipt
        assert "Price: 200" in receipt

    def test_get_receipt_with_ingredients(self, burger, mock_bun, mock_sauce):
        """Рецепт бургера с ингредиентами"""
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        receipt = burger.get_receipt()
        assert "= sauce hot sauce =" in receipt
        assert "(==== black bun ====)" in receipt

    def test_get_receipt_format(self, burger, mock_bun, mock_sauce, mock_filling):
        """Проверка формата рецепта"""
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        receipt = burger.get_receipt()
        
        assert receipt.startswith("(==== black bun ====)")
        assert "= sauce hot sauce =" in receipt
        assert "= filling cutlet =" in receipt
        assert "Price: 450" in receipt
# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division
def test_mask1():
    assert all_division(1,1) == 1

@pytest.mark.smoke
def test2():
    assert all_division(0,1) == 0

@pytest.mark.smoke
def test3():
    assert all_division(8,4) == 2

def test_mask4():
    assert all_division(9,2) == 4.5

def test_zero():
    assert all_division(1,0) == 0
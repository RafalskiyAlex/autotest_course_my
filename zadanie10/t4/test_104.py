# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.


import pytest
import time


class Test:

    def test1(self, test_time_fixture):
        time.sleep(1)

    def test2(self, test_time_fixture):
        assert ((14 / 2)**2)**0.5 == 7

    def test3(self, test_time_fixture, test_fixture):
        time.sleep(3)

    def test4(self, test_time_fixture, test_fixture):
        assert 2+2 ==4
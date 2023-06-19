# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

@pytest.mark.parametrize('a,b,result',[(1, 1, 1),
                                       (8, 4, 2),
                                       (0, 1, 0),
                                       pytest.param(9, 2, 4.5, marks=pytest.mark.smoke),
                                       pytest.param(1, 0, 0, marks=pytest.mark.skip('bad test'))])
def test_param(a, b, result):
    assert all_division(a, b) == result
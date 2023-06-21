import pytest
import datetime

@pytest.fixture(scope='class')
def test_time_fixture():
    start_time = datetime.datetime.now().strftime('%d.%m %H:%M:%S')
    yield start_time
    end_time = datetime.datetime.now().strftime('%d.%m %H:%M:%S')
    print(f'Начало выполнения: {start_time} , Окончание: {end_time}')

@pytest.fixture()
def test_fixture():
    start_time = datetime.datetime.now()
    yield start_time
    end_time = datetime.datetime.now()
    time = start_time - end_time
    fixture_time = time.total_seconds()
    print(f'Выполнения: {fixture_time}')

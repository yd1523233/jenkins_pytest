import pytest
import allure


@allure.title("this is tittle")
def test_1():
    assert 1 == 0


@allure.title("这个是第二个用例的标题")
@allure.description("这个是case的描述")
def test_2():
    assert 1 == 1


@pytest.mark.skip(reason="there is no reason, give up!!")
@allure.label('this is a labl')
def test_3():
    assert True

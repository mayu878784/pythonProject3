import pytest
import sys

#@pytest.mark.skip
def test_1():
    a = 10
    b = 20
    assert a + b == 30
    print("I am done")
    ## if asssert is true then - test case passed
    ## if assert is false then - test case failed

#### sys.version_info => (3, 10)


@pytest.mark.skipif(sys.version_info < (3, 10), reason='Python version not supported')
def test_2():
    print(sys.version_info < (3, 10))
    a = 20
    b = 20
    assert a + b == 30
    print("I am done")


@pytest.mark.xfail
def test_t4():
    a = 10
    b = 20
    assert a == b
    print("I am done")


def test_t4():   ## invalid # funciton name has to be start with test
    a = 10
    b = 10
    assert a == b
    print("I am done")


def some_test():     ## invalid # funciton name has to be start with test
    a = 10
    b = 10
    assert a == b
    print("I am done")
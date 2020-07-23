import pytest

from tester.pure_functions.case_3_exceptions import i_will_raise_exception


def test_exception_not_raised():
    test_output = i_will_raise_exception(1)
    assert test_output == 3


def test_exception_not_raised():
    with pytest.raises(Exception) as excinfo:
        test_output = i_will_raise_exception(0)
    assert "here is the exception for num 0" in str(excinfo)

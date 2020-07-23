import pytest

from tester.pure_functions.case_3_exceptions import i_will_raise_exception


'''
Read the code of function i_will_raise_exception.
It raises an exception "here is the exception for num 0" if pass integer 0 as argument.

The first test case tests the case when the function runs successfully.

The second  case uses pytest.raises function which catches any exception that is created
during code execution, and here it stores the exception value in object excinfo.
We can ask pytest to read only specific exceptions like - pytest.raises(AttributeError)
To retrieve the value in exception we have to convert it to string 
'''
def test_exception_not_raised():
    test_output = i_will_raise_exception(1)
    assert test_output == 3


def test_exception_not_raised():
    with pytest.raises(Exception) as excinfo:
        test_output = i_will_raise_exception(0)
    assert "here is the exception for num 0" in str(excinfo)

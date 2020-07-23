import pytest

from tester.pure_functions.case_11_parameterization import execute_command


'''
Paramterized tests are written when the same functions has to be tested for different inputs.

The first two test cases are similar except the input data.
'''
def test_execute_command_1():
    test_output = execute_command("")
    assert "results of "


def test_execute_command_2():
    test_output = execute_command("some command")
    assert "results of some command"


#parameterized test
@pytest.mark.parametrize("input_cmd, expected_output", [
    ("command 1","results of command 1"),
    ("command 2","results of command 2"),
    ("command 3","results of command 3"),
    ("command 4","results of command 4"),
])
def test_execute_command(input_cmd, expected_output):
    test_output = execute_command(input_cmd)
    assert test_output == expected_output
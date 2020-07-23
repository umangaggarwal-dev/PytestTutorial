from tester.pure_functions.case_1 import simplest_function

'''
The simplest case with pytest is when a function returns an output
without using any third party.

To test we just have to add a function, call the function to be tested with the required input.

Pytest follows the following nomenclature for the testing function -
1) the name of the test file should either start or end with word test, e.g. test_k.py or k_test.py
2) name of the testing function must start with word test.

keyword 'assert' is used to check if the output of tested function matches the expected output provided
if yes, the test passes
else, test fails with an AssertionError
'''
def test_simplest_function():
    test_output = simplest_function("test")
    assert test_output == {"out": "test"}

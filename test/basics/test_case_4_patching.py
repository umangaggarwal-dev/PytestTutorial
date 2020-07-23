import os

from tester.pure_functions.case_4_patching import run_os


'''
Now that we know how to write some basic test cases, we should understand the concepts of mocking.
Python's fundamental testing library unittest introduced two ways to handle third party dependencies - 
mock and patch.

A patch replaces a function or property of an object with a mock piece of code,
that by default does nothing, but we can make it return a certain value, 
that is used in our tested function.
'''
def test_run_os(mocker):
    mocker.patch.object(os, "getcwd").return_value = "blah"
    test_output = run_os()
    assert test_output == "blah"

import os

from tester.pure_functions.case_4_patching import run_os


def test_run_os(mocker):
    mocker.patch.object(os, "getcwd").return_value = "blah"
    test_output = run_os()
    assert test_output == "blah"

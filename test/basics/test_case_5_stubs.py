import subprocess

import pytest

from tester.pure_functions.case_5_stubs import run_subprocess


'''
Patching becomes very powerful tool, since we can replace every reference to a certain
object or code with a stub, that acts as a mock and returns values as we desire.

A stub can be a class or function that is used as a patch against the original object.

Here we create a MockPopen class, which has a mock communicate function,
instance of MockPopen is returned when subprocess.Popen is called,
this instance has method communicate which returns mock values when called.

Stub popen_stub replaces the subprocess.Popen() and returns an instance of class MockPopen.

Another strange thing that should be noticed, is the paramter "mocker" in the test case test_run_subprocess.
It is a fixture created by pytest, or to be specific it is created by the dependency pytest-mock
that we installed while setting up the environment.
We will understand it better in the chapter "Working with mock".  
'''
#stubs
@pytest.fixture(name="mock_popen")
def get_mock_popen():
    class MockPopen:
        def communicate(self, *args, **kwargs):
            return "", ""
    yield MockPopen


@pytest.fixture(name="popen_stub")
def get_popen_stub(mock_popen):
    def popen_stub(*args, **kwargs):
        return mock_popen()
    yield popen_stub


def test_run_subprocess(mocker, popen_stub):
    mocker.patch.object(subprocess, "Popen", new=popen_stub)
    test_output = run_subprocess()
    assert test_output == ""

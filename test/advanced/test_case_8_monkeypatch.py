import subprocess

import pytest

from tester.pure_functions.case_5_stubs import run_subprocess


'''
Monkeypatch is an alternate to unittest patch, and is native to pytest.
We should understand that there is no added advantage of monkeypatch over a normal mocker.patch
infact monkeypatch being a fixture has the inherent risks of a fixture,
but sometimes monkeypatch can reduce the code to some extent.

Here we are revisiting the code of test case 5,
look at the differences, 
we are no longer creating a mock class manually since we already know how to use Mock 
'''
@pytest.fixture(name="mock_popen")
def get_mock_popen(mocker):
    mock_popen = mocker.Mock(spec=subprocess.Popen)
    mock_popen.communicate.return_value = ("blah", "")
    return mock_popen


@pytest.fixture(name="popen_stub")
def get_popen_stub(mock_popen):
    def popen_stub(*args, **kwargs):
        return mock_popen
    yield popen_stub


def test_run_subprocess_revisited(monkeypatch, popen_stub):
    monkeypatch.setattr(subprocess, "Popen", popen_stub)
    test_output = run_subprocess()
    assert test_output == "blah"
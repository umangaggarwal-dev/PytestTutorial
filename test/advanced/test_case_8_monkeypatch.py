import subprocess

import pytest

from tester.pure_functions.case_5_stubs import run_subprocess


@pytest.fixture(name="mock_popen")
def get_mock_popen(mocker):
    mock_popen = mocker.Mock(spec=subprocess.Popen)
    mock_popen.communicate.return_value = ("blah","")
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
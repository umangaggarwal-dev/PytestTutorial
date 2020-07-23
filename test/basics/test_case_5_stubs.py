import subprocess

import pytest

from tester.pure_functions.case_5_stubs import run_subprocess


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

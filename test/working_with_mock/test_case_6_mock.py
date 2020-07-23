from unittest.mock import Mock

import pytest

from tester.classes.db_connection import DbConnection
from tester.classes.foo import Foo


'''
Python's unittest library has the module mock, which was added to it after python 3.3,
for earlier versions we have to install this module with - pip install mock

Function Mock of module mock creates a mock instance of any class,
which is specified with the "spec" parameter, although it does not implement any of the functions.

We can define the return value of any function or property of the mock instance,
by defining a value of mock_instance.<function or property>.return_value

We are using a module of unittest, because pytest is written as enhancement over unittest.
Infact patching which we used earlier is also a part of unittest library,
which we used using mocker fixture of pytest, but it actually utilizes modules of unittest.
'''
@pytest.fixture(name="mock_db")
def get_mock_db():
    mock_db = Mock(spec=DbConnection)
    mock_db.get_data
    return mock_db


def test_data_peristence(mock_db):
    mock_db.get_data.return_value = "blah"
    blah = Foo(con=mock_db)
    blah.set_data("umang")
    assert blah.get_data() == "blah"

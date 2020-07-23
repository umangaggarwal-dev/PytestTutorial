from unittest.mock import Mock

import pytest

from tester.classes.db_connection import DbConnection
from tester.classes.foo import Foo


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

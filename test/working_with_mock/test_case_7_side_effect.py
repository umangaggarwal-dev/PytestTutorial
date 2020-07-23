import pytest
import json

from tester.classes.foo import Foo
from tester.classes.service import Service


#side effect stub
@pytest.fixture(name="process_data_stub")
def get_process_data_stub():
    def process_data_stub(string):
        return json.loads(string)
    yield process_data_stub


@pytest.fixture(name="mock_service")
def get_mock_service(mocker, process_data_stub):
    mock_service = mocker.Mock(spec=Service)
    mock_service.process_data.side_effect = process_data_stub
    return mock_service


def test_blah_using_service(mock_service):
    test_json = "{\"test\":\"test\"}"
    blah = Foo(service=mock_service)
    output = blah.process_data(test_json)
    assert output == {"test": "test"}
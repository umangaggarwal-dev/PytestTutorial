from tester.classes.stack import Stack


def test_create_stack_using_mock(mocker):
    mock_stack = mocker.Mock(spec = Stack)
    assert len(mock_stack) == 0


def test_create_stack_using_magicmock(mocker):
    mock_stack = mocker.MagicMock(spec = Stack)
    assert len(mock_stack) == 0

def test_create_stack_using_magicmock_2(mocker):
    mock_stack = mocker.MagicMock(spec=Stack)
    mock_stack.__len__.return_value = 3
    assert len(mock_stack) == 3
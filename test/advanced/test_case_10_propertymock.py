from tester.classes.stack import Stack


'''
A property mock is used to replace a certain property (variable or function)
of a class, it comes handy when we have to write test cases which utilizes user defined classes.

The first case simply patches function get_data of class Stack.

The second case binds a PropertyMock object to a MagicMock instance of class Stack. 
'''
def test_use_propertymock_on_stack(mocker):
    patch = mocker.patch.object(Stack, "get_data", new_callable=mocker.PropertyMock)
    patch.return_value = "blah"
    stack = Stack([1, 2, 3])
    assert stack.get_data == "blah"


def test_use_propertymock_with_mock_stack(mocker):
    mock_stack = mocker.MagicMock(spec=Stack)
    mock_data = mocker.PropertyMock(return_value="blah")
    type(mock_stack).data = mock_data
    assert mock_stack.data == "blah"
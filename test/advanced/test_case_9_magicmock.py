from tester.classes.stack import Stack


'''
MagicMock is a child class of Mock, which automatically implements all the magic function of Python.

A magic function in python is used by functions (and generators) like list(), print(), len().
To make len() generator work on a class, we have to define __itr__ magic method in that class.
If you look at the code of class Stack, we have implemented __len__ which is used by function len().

The first test case uses Mock, which does not automatically implements the magic functions.
The second case uses MagicMock, and it passes.
MagicMock implements all the magic functions of python by default, however
if we specify a class in argument spec, it will only implement the magic functions
that are defined in the reference class, 
in our case it will only implement magic functions of class Stack  
'''
#test will fail
def test_create_stack_using_mock(mocker):
    mock_stack = mocker.Mock(spec=Stack)
    assert len(mock_stack) == 0


#test will pass
def test_create_stack_using_magicmock(mocker):
    mock_stack = mocker.MagicMock(spec=Stack)
    assert len(mock_stack) == 0


#test will pass
def test_create_stack_using_magicmock_2(mocker):
    mock_stack = mocker.MagicMock(spec=Stack)
    mock_stack.__len__.return_value = 3
    assert len(mock_stack) == 3
import pytest
import yaml
from tester.pure_functions.case_2_fixtures import get_path


'''
Pytest fixtures allow dependency injection for the test cases.
Fixtures are created before the unit tests and their value is injected into the test cases
by adding the name of fixture as parameter in the test definition.

For more benefits of fixtutres read about - 
 - pytest fixture scope
 - pytest fixture autouse
 
Despite the advantages, fixtures have risk of fixture leaking and duplication,
which should be taken care of.
'''
@pytest.fixture(name="test_configs")
def get_test_configs():
    with open("test_config.yml", 'r') as file:
        configs = yaml.load(file, Loader=yaml.FullLoader)
    return configs


def test_get_path(test_configs):
    test_output = get_path(test_configs)
    assert test_output == "~/Docs"
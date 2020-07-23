import pytest
import yaml
from tester.pure_functions.case_2_fixtures import get_path


@pytest.fixture(name="test_configs")
def get_test_configs():
    with open("test_config.yml", 'r') as file:
        configs = yaml.load(file, Loader=yaml.FullLoader)
    return configs


def test_get_path(test_configs):
    test_output = get_path(test_configs)
    assert test_output == "~/Docs"
import pytest


@pytest.fixture
def fix_config():
    arg = [1, 2, 3, 4, 5]
    str1 = 'strinf_argument'
    return str1, arg

def test_run(fix_config):
    print(list(fix_config))
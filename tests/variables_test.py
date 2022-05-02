import os
from evpython import load_environment

def test_should_load_environment_variables_using_inline_secret():
    load_environment(secret='ev-python#password')
    assert os.getenv('VARIABLE_NAME') == 'my-variable-content'

from evpython import __version__, load_environment

def test_version():
    assert __version__ == '0.1.0'

def test_exports_a_function():
    assert load_environment is not None
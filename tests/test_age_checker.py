from lib.age_checker import *

def test_age_over_16():
    result = age_checker('2001-07-08')
    assert result == "Access granted"


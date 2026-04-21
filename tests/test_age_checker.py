from lib.age_checker import *
import pytest

def test_age_over_16():
    result = age_checker('2001-07-08')
    assert result == "Access granted"

def test_age_under_16():
    result = age_checker("2011-01-01")
    assert result == "Access denied. You are 15, and the required age is 16."

def test_age_16():
    result = age_checker("2010-01-08")
    assert result == "Access granted"



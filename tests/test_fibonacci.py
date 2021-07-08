from app.fibonacci import *
import pytest

def test_fib():
    for (i,o) in [(3,2)]:
        assert fib(i) == o

def test_fib_type_error():
    with pytest.raises(TypeError):
        fib(1.5)

def test_fib_value_error():
    with pytest.raises(ValueError):
        fib(-1)